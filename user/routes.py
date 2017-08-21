from flask import Blueprint, render_template
import bcrypt

from user.models import User
from user.forms import RegisterForm

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/login')
def login():
    return 'user login'

@user_routes.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            username=form.username.data,
            password=hashed_password,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data
            )
        user.save()
        return "User registered"
    return render_template('user/register.html', form=form)