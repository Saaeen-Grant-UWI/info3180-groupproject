### Group Members ###
# Roshaun Marshall - 620154268
# Saaeen Grant - 620155794
# Tariq Davy - 620154200
# Paul Bailey - 620154531
# Rahjay Jones - 620154157


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/jamdate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretckey'

db.init_app(app)
migrate.init_app(app, db)

from app import routes, models

if __name__ == '__main__':
    app.run()
