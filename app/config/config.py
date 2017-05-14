# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~~~~~~~~~~~~~~

    flask config file.

    :copyright: (c) 2017 by Blurt Heart.
    :license: BSD, see LICENSE for more details.
"""

import os
import logging


__all__ = ['config']


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SERVER_NAME = '0.0.0.0:8000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Can You Guess Out?'
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[flask-oauth2-server]'
    FLASKY_MAIL_SENDER = 'flask-oauth2-server admin <%s>' %MAIL_USERNAME
    FLASKY_ADMIN = "administrator@test.com"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGER_NAME = 'mylogger.log'


class DevelopmentConfig(Config):
    DEBUG = True
    LOGGER_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    LOGGER_LEVEL = logging.DEBUG
    LOGGER_NAME = 'test-flask.log'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    FLASKY_ADMIN = "administrator@test.com"


config = {
    'development': DevelopmentConfig,
    'default':DevelopmentConfig,
    'testing':TestingConfig
}