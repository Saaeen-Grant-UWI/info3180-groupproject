from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/jamdate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
    


if __name__ == '__main__':
    app.run()