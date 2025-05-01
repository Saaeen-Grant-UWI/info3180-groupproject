from app import db
from datetime import datetime

####### USER MODEL #######
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # You should store a hashed password
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(200))  # This could be a URL or file path
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    # One-to-one relationship with Profile
    profile = db.relationship('Profile', back_populates='user', uselist=False)

    # Relationships for favourites
    favourites_given = db.relationship('Favourite', foreign_keys='Favourite.user_id_fk', back_populates='user')
    favourites_received = db.relationship('Favourite', foreign_keys='Favourite.fav_user_id_fk', back_populates='fav_user')

    def __repr__(self):
        return f'<User {self.username}>'
    

####### PROFILE MODEL #######
class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255))
    parish = db.Column(db.String(100))
    biography = db.Column(db.Text)
    sex = db.Column(db.String(10))
    race = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    height = db.Column(db.Float)
    fav_cuisine = db.Column(db.String(100))
    fav_colour = db.Column(db.String(50))
    fav_school_subject = db.Column(db.String(100)) 
    political = db.Column(db.Boolean, default=False)
    religious = db.Column(db.Boolean, default=False)
    family_oriented = db.Column(db.Boolean, default=False)

    # Link to user
    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f'<Profile for User ID {self.user_id_fk}>'
    

####### FAVOURITE MODEL #######
class Favourite(db.Model):
    __tablename__ = 'favourites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fav_user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=[user_id_fk], back_populates='favourites_given')
    fav_user = db.relationship('User', foreign_keys=[fav_user_id_fk], back_populates='favourites_received')

    def __repr__(self):
        return f'<Favourite: User {self.user_id_fk} -> User {self.fav_user_id_fk}>'
