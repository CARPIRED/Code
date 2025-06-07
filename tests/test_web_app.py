"""Flask route tests executed with pytest, skipped if Flask is unavailable."""

import importlib.util
import pytest

flask_spec = importlib.util.find_spec("flask")
if flask_spec is None:
    pytest.skip("Flask not installed", allow_module_level=True)

from web.app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data


def test_index_post_report(client):
    data = {
        'findings': 'nodule in lung',
        'image_path': 'chest.png',
        'age': '60',
        'sex': 'M',
        'task': 'report',
    }
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'response' in response.data
