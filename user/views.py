from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/login')
def login():
    return 'user login'
