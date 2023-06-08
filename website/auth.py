from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/about')
def login():
    return "<h1>Login</h1>"


@auth.route('/logout')
def logout():
    return "<h1>logout<h1>"
