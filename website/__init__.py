from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9ogb73wgw7r608br8yv&Tg80$tbaw4b8y02v4t239b0981!^B$2vt9812cnb89b81vb98ashiounm3vh7q0m2nvnrqyh08'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')

    return app
