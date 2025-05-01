from app import app, db
from app.models import User, Profile, Favourite
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from datetime import datetime

@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Hello, World!")

####### ROUTE TO REGISTER A USER #######
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json

    # Extract fields
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    email = data.get('email')
    photo = data.get('photo')  # Could be a URL or base64 string

    # Basic validation
    if not all([username, password, name, email]):
        return jsonify(error="All fields (username, password, name, email) are required."), 400

    # Check if username or email already exists
    if User.query.filter_by(username=username).first():
        return jsonify(error="Username already taken."), 409
    if User.query.filter_by(email=email).first():
        return jsonify(error="Email already registered."), 409
    

    # Hash the password
    hashed_password = generate_password_hash(data['password'])



    # Create new user instance
    new_user = User(
        username=username,
        password=hashed_password,
        name=name,
        email=email,
        photo=photo or '',
        date_joined=datetime.utcnow()
    )

    # Save to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User registered successfully"), 201


####### ROUTE TO LOGIN A USER #######
@app.route('/api/auth/login', methods=['POST'])
def login_user():
    data = request.json

    if not data or not data.get('username') or not data.get('password'):
        return jsonify(error="Username and password are required"), 400

    user = User.query.filter_by(username=data['username'], password=data['password']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify(error="Invalid username or password"), 401

    return jsonify(message="User logged in successfully", user_id=user.id), 200

####### ROUTE TO LOGOUT A USER #######
@app.route('/api/auth/logout', methods=['POST'])
def logout_user():
    # Logic to logout user
    return jsonify(message="User logged out successfully"), 200

####### ROUTE TO GET ALL PROFILES #######
@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    # Logic to return all profiles
    return jsonify(profiles=[]), 200

####### ROUTE TO ADD A NEW PROFILE #######
@app.route('/api/profiles', methods=['POST'])
def add_profile():
    data = request.json
    # Logic to add a new profile
    return jsonify(message="Profile added successfully"), 201

####### ROUTE TO GET DETAILS OF A SPECIFIC PROFILE #######
@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    # Logic to get profile details
    return jsonify(profile={}), 200

####### ROUTE TO ADD A USER TO FAVOURITES #######
@app.route('/api/profiles/<int:user_id>/favourite', methods=['POST'])
def add_to_favourites(user_id):
    # Logic to add user to favourites
    return jsonify(message="User added to favourites"), 201

####### ROUTE TO GET MATCHING PROFILES
@app.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
def get_matching_profiles(profile_id):
    # Logic to get matching profiles
    return jsonify(matches=[]), 200

####### ROUTE TO SEARCH FOR PROFILES #######
@app.route('/api/search', methods=['GET'])
def search_profiles():
    # Logic to search profiles by criteria
    return jsonify(results=[]), 200

####### ROUTE TO GET DETAILS OF A USER #######
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Logic to get user details
    return jsonify(user={user_id}), 200

####### ROUTE TO GET USERS THAT A USER HAS FAVOURED #######
@app.route('/api/users/<int:user_id>/favourites', methods=['GET'])
def get_user_favourites(user_id):
    # Logic to get user's favourites
    return jsonify(favourites=[]), 200

####### ROUTE TO GET THE TOP N FAVOURED USERS #######
@app.route('/api/users/favourites/<int:n>', methods=['GET'])
def get_top_favoured_users(n):
    # Logic to get top N favoured users
    return jsonify(top_favourites=[]), 200