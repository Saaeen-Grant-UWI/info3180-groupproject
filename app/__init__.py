### Group Members ###
# Roshaun Marshall - 620154268
# Saaeen Grant - 620155794
# Tariq Davy - 620154200
# Paul Bailey - 620154531
# Rahjay Jones - 620154157


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)
migrate.init_app(app, db)
CORS(app)

from app import routes, models 