# -*- coding: utf-8 -*-
"""
    __init__
    ~~~~~~~~~~~~~~~~~~~

    create a flask app and init it.

    :copyright: (c) 2017 by Blurt Heart.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config.config import config


__all__ = ['db', 'login_manager', 'oauth', 'create_app']


db = SQLAlchemy()

from .oauth2_provider import default_provider
oauth = default_provider()
login_manager = LoginManager()
login_manager.session_protection = 'strong'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # logger setting
    import logging
    from logging.handlers import RotatingFileHandler
    _handler = RotatingFileHandler(app.config['LOGGER_NAME'], maxBytes=10000, backupCount=1)
    _handler.setLevel(app.config['LOGGER_LEVEL'])
    app.logger.addHandler(_handler)

    # init app
    db.init_app(app)
    oauth.init_app(app)
    login_manager.init_app(app)
    app.secret_key = app.config['SECRET_KEY']

    # register views
    from .api import api
    app.register_blueprint(api)
    return app