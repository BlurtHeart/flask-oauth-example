#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    server
    ~~~~~~~~~~~~~~~~~~~

    provide an oauth2 api.

    :copyright: (c) 2017 by Blurt Heart.
    :license: BSD, see LICENSE for more details.
"""

from datetime import datetime, timedelta
from app import create_app, db
from app.models import Client, User, Grant, Token


# def prepare_db():
#     db.create_all()

#     client1 = Client(
#         name='dev', client_id='dev', client_secret='dev',
#         _redirect_uris=(
#             'http://localhost:8000/authorized '
#             'http://localhost/authorized '
#             'http://127.0.0.1:8000/authorized'
#         ),
#     )

#     client2 = Client(
#         name='confidential', client_id='confidential',
#         client_secret='confidential', client_type='confidential',
#         _redirect_uris=(
#             'http://localhost:8000/authorized '
#             'http://localhost/authorized'
#         ),
#     )

#     user = User(username='admin', password='111111')

#     temp_grant = Grant(
#         user_id=1, client_id='confidential',
#         code='12345', scope='email',
#         expires=datetime.utcnow() + timedelta(seconds=100)
#     )

#     access_token = Token(
#         user_id=1, client_id='dev', access_token='expired', expires_in=0
#     )

#     access_token2 = Token(
#         user_id=1, client_id='dev', access_token='never_expire'
#     )

#     try:
#         db.session.add(client1)
#         db.session.add(client2)
#         db.session.add(user)
#         db.session.add(temp_grant)
#         db.session.add(access_token)
#         db.session.add(access_token2)
#         db.session.commit()
#     except:
#         db.session.rollback()


if __name__ == '__main__':
    app = create_app('development')
    # prepare_db()
    app.run()
