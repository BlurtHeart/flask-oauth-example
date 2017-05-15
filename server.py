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


def prepare_db():
    client1 = Client(
        name='dev', client_id='dev', client_secret='dev',
        _redirect_uris=(
            'http://localhost:8000/authorized '
            'http://localhost/authorized '
            'http://127.0.0.1:8000/authorized'
        ),
    )

    client2 = Client(
        name='confidential', client_id='confidential',
        client_secret='confidential', client_type='confidential',
        _redirect_uris=(
            'http://localhost:8000/authorized '
            'http://localhost/authorized '
            'http://127.0.0.1:8000/authorized'
        ),
    )

    user = User(username='admin', password='111111')

    temp_grant = Grant(
        user_id=1, client_id='confidential',
        code='12345', scope='email',
        expires=datetime.utcnow() + timedelta(seconds=100)
    )

    access_token = Token(
        user_id=1, client_id='dev', access_token='expired', expires_in=5
    )

    access_token2 = Token(
        user_id=1, client_id='dev', access_token='expired', expires_in=1
    )

    try:
        db.session.add(client1)
        db.session.add(client2)
        db.session.add(user)
        db.session.add(temp_grant)
        db.session.add(access_token)
        db.session.add(access_token2)
        db.session.commit()
    except:
        db.session.rollback()


# debug
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w')
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    app = create_app('development')
    context = app.app_context()
    context.push()
    db.create_all()
    prepare_db()
    app.run()
