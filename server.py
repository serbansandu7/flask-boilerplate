"""
    The Python server entry point.
"""

from flask import Flask
from flask_cors import CORS

import settings
from database_management import init_database_connection, build_connection_string
from src.blueprints.user_blueprint import user_blueprint


def configure_app(application):

    connection_string = build_connection_string(
        settings.DB_HOST, settings.DB_USER, settings.DB_PASSWORD, settings.DB_PORT, settings.DB_NAME
    )
    application.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    init_database_connection(connection_string)


app = Flask(__name__)
CORS(app)
configure_app(app)
app.register_blueprint(user_blueprint)


def main():
    """
        Fii practic - Server main
    """
    app.run(threaded=True)
