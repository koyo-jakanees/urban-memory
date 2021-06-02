from flask import Blueprint, render_template
from flask import current_app as app

view = Blueprint("view", __name__)

@view.route("/")
def index():

    app.logger.debug(app.config.get("ENV"))

    return "Hello world!"
