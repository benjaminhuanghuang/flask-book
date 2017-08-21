from flask import Flask
from flask.ext.mongoengine import MongoEngine
#
from user.views import user_routes


db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    app.register_blueprint(user_routes)
    return app
