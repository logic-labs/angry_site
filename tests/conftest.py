import os
import tempfile

import pytest
from angry_site_flask import create_app
from angry_site_flask.db_psql import init_db
import data_sql


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)

@pytest.fixture
def app():
    # db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        "TESTING": True,
        # "DATABASE": db_path
    })

    with app.app_context():
        init_db()
        # get_db().executescript(_data_sql)
        data_sql.prfrm_test()

    yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
