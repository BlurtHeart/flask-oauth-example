# -*- coding: utf-8 -*-
"""
    api
    ~~~~~~~~~~~~~~~~~~~

    create api blueprint and add rules for it.

    :copyright: (c) 2017 by Blurt Heart.
    :license: BSD, see LICENSE for more details.
"""

from flask import Blueprint, redirect, url_for, jsonify, make_response, request, \
                render_template, current_app
from flask_login import login_user, logout_user, \
     login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, identity_changed                     
from . import oauth
from .models import User


api = Blueprint('api', __name__)


@api.route('/oauth/authorize', methods=['GET', 'POST'])
@oauth.authorize_handler
def authorize(*args, **kwargs):
    print 'enter authorize'
    # NOTICE: for real project, you need to require login
    if request.method == 'GET':
        # render a page for user to confirm the authorization
        # return render_template('confirm.html')
        return render_template('xlogin.html')
    if request.method == 'HEAD':
        # if HEAD is supported properly, request parameters like
        # client_id should be validated the same way as for 'GET'
        response = make_response('', 200)
        response.headers['X-Client-ID'] = kwargs.get('client_id')
        return response
    # confirm = request.form.get('confirm', 'no')
    # return confirm == 'yes'
    username = request.form.get('username')
    password = str(request.form.get('password'))
    user = User.query.filter_by(username=username).first()
    result = False
    if user is not None and user.check_password(password):
        login_user(user)
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
        result = True
    return result


@api.route('/xlogout')
@login_required
def logout():
    logout_user()
    return jsonify({'result':'user logout'})


@api.route('/oauth/token', methods=['POST', 'GET'])
@oauth.token_handler
def access_token():
    return {}


@api.route('/oauth/revoke', methods=['POST'])
@oauth.revoke_handler
def revoke_token():
    pass


@api.route('/api/email')
@oauth.require_oauth('email')
def email_api():
    oauth = request.oauth
    return jsonify(email='me@oauth.net', username=oauth.user.username)


@api.route('/api/client')
@oauth.require_oauth()
def client_api():
    oauth = request.oauth
    return jsonify(client=oauth.client.name)


@api.route('/api/address/<city>')
@oauth.require_oauth('address')
def address_api(city):
    oauth = request.oauth
    return jsonify(address=city, username=oauth.user.username)


@api.route('/api/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
@oauth.require_oauth()
def method_api():
    return jsonify(method=request.method)


@api.route('/oauth/errors')
def error():
    return 'something goes wrong'


@api.route('/xlogin', methods=['GET', 'POST'])
def xlogin():
    if request.method == 'GET':
        return render_template('xlogin.html')
    referer = request.headers.get('Referer')
    print 'referer:', referer
    return redirect(referer)


@oauth.invalid_response
def require_oauth_invalid(req):
    return jsonify(message=req.error_message), 401
