import unittest
import json
from app import app


class DefaultTestCase(unittest.TestCase):

    def setUp(self):
        api = app.test_client()
        self.response = api.get('/')

    def test_content(self):
        self.assertEqual(200, self.response.status_code)
        self.assertEqual(b'Desafio Captalys', self.response.data)


class TestRepositoryUser(unittest.TestCase):

    def setUp(self):
        api = app.test_client()
        self.response = api.get('/repository/user/bruno-m-santos')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual(b'["AkkaStream", "kafkaltsamples", "lt"]', self.response.data)


class TestRepository(unittest.TestCase):

    def setUp(self):
        api = app.test_client()
        self.response = api.get('repository/user/bruno-m-santos/lt')

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual('bruno-m-santos/lt', json.loads(self.response.data)['full_name'])


if __name__ == '__main__':
    unittest.main()
