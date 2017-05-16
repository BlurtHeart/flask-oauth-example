# -*- coding: utf-8 -*-
"""
    manager api
    ~~~~~~~~~~~~~~~~~~~

    manage the developer information.

    :copyright: (c) 2017 by Blurt Heart.
    :license: BSD, see LICENSE for more details.
"""

from flask import request, jsonify, redirect, url_for, abort, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from flask_principal import identity_changed
import uuid


manager = Blueprint(__name__)


@manager.route('/application', methods=['POST'])
@login_required
def application():
    if request.json is None:
        abort(400)
    req = request.json
    app_name = req.get('appname', None)
    app_desc = req.get('appdesc', None)
    if None in (app_name, app_desc):
        abort(400)

    # generate client_id and client_secret
    client_id = uuid.uuid1()
    client_secret = uuid.uuid1()
    return jsonify({
            'appname':app_name,
            'appdesc':app_desc,
            'client_id':client_id,
            'client_secret':client_secret
        })


@manager.route('/login', methods=['POST'])
def login():
    if request.json is None:
        abort(400)
    req = request.json
    username = req.get('username', None)
    password = req.get('password', None)
    if None in (username, password):
        abort(400)
    # check user and password
    result = 0
    return jsonify({'result':result, 'user':username})