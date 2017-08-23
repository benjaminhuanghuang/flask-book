from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)

    db.init_app(app)

    from user.routes import user_routes
    app.register_blueprint(user_routes)

    from relationship.views import relationship_app
    app.register_blueprint(relationship_app)

    from feed.views import feed_app
    app.register_blueprint(feed_app)

    from home.routes import home_routes
    app.register_blueprint(home_routes)

    return app