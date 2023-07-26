from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9ogb73wgw7r608br8yv&Tg80$tbaw4b8y02v4t239b0981!^B$2vt9812cnb89b81vb98ashiounm3vh7q0m2nvnrqyh08'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')

    from .models import User, Note

    return app

def create_database(app):
    if not path('website/' + DB_NAME):
        db.create_all(app=app)
        print('created Database!')