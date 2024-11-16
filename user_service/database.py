from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Carga las variables de entorno
load_dotenv()

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgre:1234@localhost:5432/mascotas')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
