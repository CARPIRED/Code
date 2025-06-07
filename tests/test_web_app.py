import importlib.util
import pytest

if importlib.util.find_spec("flask") is None:
    pytest.skip("Flask not installed", allow_module_level=True)

from web.app import app


def test_index_get():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data


def test_index_post_report():
    client = app.test_client()
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

