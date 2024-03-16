from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from os import environ

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from .models import Transporte
        db.create_all() 

    from .routes import initialize_routes
    api = Api(app)
    initialize_routes(api)

    return app