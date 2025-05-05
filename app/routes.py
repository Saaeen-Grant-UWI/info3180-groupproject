from flask import jsonify, request
from app import app, db
from app.models import User, Profile, Favourite
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]

        if not token:
            return jsonify(error='Token is missing!'), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except Exception as e:
            return jsonify(error='Token is invalid or expired!'), 401

        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/')
def index():
    return jsonify(message="Hello, World!")

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    email = data.get('email')
    photo = data.get('photo')

    if not all([username, password, name, email]):
        return jsonify(error="All fields are required."), 400

    if User.query.filter_by(username=username).first():
        return jsonify(error="Username already taken."), 409
    if User.query.filter_by(email=email).first():
        return jsonify(error="Email already registered."), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, name=name, email=email, photo=photo or '')
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User registered successfully"), 201

@app.route('/api/auth/login', methods=['POST'])
def login_user():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify(error="Username and password are required"), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify(error="Invalid credentials"), 401

    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify(message="Login successful", token=token), 200

@app.route('/api/auth/logout', methods=['POST'])
def logout_user():
    return jsonify(message="User logged out successfully"), 200

@app.route('/api/profiles', methods=['GET'])
@token_required
def get_profiles(current_user):
    profiles = Profile.query.order_by(Profile.created_at.desc()).limit(4).all()
    return jsonify(profiles=[p.to_dict() for p in profiles]), 200

@app.route('/api/profiles', methods=['POST'])
@token_required
def add_profile(current_user):
    data = request.json
    try:
        profile = Profile(
            user_id_fk=current_user.id,
            biography=data['description'], 
            parish=data['parish'],
            birth_year=data['birth_year'],
            sex=data['sex'],
            race=data['race'],
            height=data['height'],
            fav_colour=data.get('fav_colour'),
            fav_cuisine=data.get('fav_cuisine'),
            fav_school_subject=data.get('fav_school_subject'),
            political=data.get('political', False),
            religious=data.get('religious', False),
            family_oriented=data.get('family_oriented', False)
        )
        db.session.add(profile)
        db.session.commit()
        return jsonify(message="Profile added successfully"), 201
    except Exception as e:
        app.logger.error(f"Profile creation failed: {e}")
        return jsonify(error=str(e)), 500


@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
@token_required
def get_profile(current_user, profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify(profile=profile.to_dict()), 200

@app.route('/api/profiles/<int:user_id>/favourite', methods=['POST'])
@token_required
def add_to_favourites(current_user, user_id):
    if Favourite.query.filter_by(user_id=current_user.id, favourite_id=user_id).first():
        return jsonify(message="Already in favourites"), 409

    fav = Favourite(user_id=current_user.id, favourite_id=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(message="User added to favourites"), 201

@app.route('/api/search', methods=['GET'])
@token_required
def search_profiles(current_user):
    query = Profile.query
    name = request.args.get('name')
    birth_year = request.args.get('birth_year')
    sex = request.args.get('sex')
    race = request.args.get('race')

    if name:
        query = query.filter(Profile.name.ilike(f"%{name}%"))
    if birth_year:
        query = query.filter_by(birth_year=birth_year)
    if sex:
        query = query.filter_by(sex=sex)
    if race:
        query = query.filter_by(race=race)

    results = [p.to_dict() for p in query.all()]
    return jsonify(results=results), 200

@app.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
@token_required
def get_matching_profiles(current_user, profile_id):
    main = Profile.query.get_or_404(profile_id)
    candidates = Profile.query.filter(Profile.id != main.id).all()
    matches = []

    for c in candidates:
        age_diff = abs(main.birth_year - c.birth_year)
        height_diff = abs(main.height - c.height)
        match_count = sum([
            main.fav_cuisine == c.fav_cuisine,
            main.fav_colour == c.fav_colour,
            main.fav_school_subject == c.fav_school_subject,
            main.political == c.political,
            main.religious == c.religious,
            main.family_oriented == c.family_oriented
        ])

        if age_diff <= 5 and 3 <= height_diff <= 10 and match_count >= 3:
            matches.append(c.to_dict())

    return jsonify(matches=matches), 200

@app.route('/api/users/<int:user_id>', methods=['GET'])
@token_required
def get_user(current_user, user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user={"id": user.id, "username": user.username, "name": user.name, "email": user.email}), 200

@app.route('/api/users/<int:user_id>/favourites', methods=['GET'])
@token_required
def get_user_favourites(current_user, user_id):
    favs = Favourite.query.filter_by(user_id=user_id).all()
    fav_ids = [f.favourite_id for f in favs]
    users = User.query.filter(User.id.in_(fav_ids)).all()
    return jsonify(favourites=[{"id": u.id, "username": u.username} for u in users]), 200

@app.route('/api/users/favourites/<int:n>', methods=['GET'])
@token_required
def get_top_favoured_users(current_user, n):
    favs = db.session.query(Favourite.favourite_id, db.func.count().label('count'))\
                .group_by(Favourite.favourite_id)\
                .order_by(db.desc('count'))\
                .limit(n).all()
    top_ids = [f.favourite_id for f in favs]
    users = User.query.filter(User.id.in_(top_ids)).all()
    return jsonify(top_favourites=[{"id": u.id, "username": u.username} for u in users]), 200