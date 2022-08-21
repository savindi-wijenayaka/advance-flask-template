from flask import Flask

from app.api.routes import api
from app.website.routes import website

from config import config

def create_app(app_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[app_config])

    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(website)
    return app
