"""Flask route tests executed with unittest, skipped if Flask is unavailable."""

import importlib.util
import unittest

FLASK_AVAILABLE = importlib.util.find_spec("flask") is not None

if not FLASK_AVAILABLE:
    raise unittest.SkipTest("Flask not installed")

from web.app import app


class TestWebApp(unittest.TestCase):
    """Basic integration tests for the Flask application."""

    def setUp(self) -> None:
        self.client = app.test_client()

    def test_index_get(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form', response.data)

    def test_index_post_report(self) -> None:
        data = {
            'findings': 'nodule in lung',
            'image_path': 'chest.png',
            'age': '60',
            'sex': 'M',
            'task': 'report',
        }
        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'response', response.data)


if __name__ == "__main__":
    unittest.main()

