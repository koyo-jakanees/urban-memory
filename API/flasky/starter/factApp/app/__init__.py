# https://pythonise.com/series/learning-flask/application-factory-pattern-|-learning-flask-ep.-30
from flask import Flask
from .utils import config

import os

def create_app(testing=False):
    """ Application factory

    Args:
        testing (bool): Will load TestingConfig if True, defaults fo False
    Returns:
        The Flask application object
    """

    app = Flask(__name__)

    # Dynamically load config based on the testing argument or FLASK_ENV environment variable
    flask_env = os.getenv("FLASK_ENV", None)
    if testing:
        app.config.from_object(config.TestingConfig)
    elif flask_env == "development":
        app.config.from_object(config.ProductionConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.ProductionConfig)

    # Import and register blueprints
    from app.blueprints.views import view
    from app.blueprints.api import api

    app.register_blueprint(view)
    app.register_blueprint(api)

    return app
