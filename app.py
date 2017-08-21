from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    '''
    can not put this line in the beginning of the file.
    app -> routers -> models -> app.db
    '''
    from user.routes import user_routes
    app.register_blueprint(user_routes)
    return app
