from flask import Flask
from flask_restful import Api
from os import environ
from dotenv import load_dotenv
from app.models import db
from app.resources import TransportePublico
from app.routes import initialize_routes

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app)
    initialize_routes(api)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
