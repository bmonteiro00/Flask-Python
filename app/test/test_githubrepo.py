import unittest
import json
from app import app
from unittest.mock import patch
from test.support import EnvironmentVarGuard


class DefaultTestCase(unittest.TestCase):

    def setUp(self):
        api = app.test_client()
        self.response = api.get('/')
        self.env = EnvironmentVarGuard()
        self.env.set('MONGODB_HOST', 'localhost')
        self.env.set('MONGODB_DATABSE', 'gitbase')


    def test_content(self):
        self.assertEqual(200, self.response.status_code)
        self.assertEqual(b'Desafio Captalys', self.response.data)


class TestRepositoryUser(unittest.TestCase):

    def setUp(self):
        api = app.test_client()
        self.response = api.get('/repository/user/bruno-m-santos')
        self.env = EnvironmentVarGuard()
        self.env.set('MONGODB_HOST', 'localhost')
        self.env.set('MONGODB_DATABSE', 'gitbase')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual(b'bruno-m-santos', self.response.data)


class TestRepository(unittest.TestCase):

    def setUp(self):
        api = app.test_client()
        self.response = api.get('repository/user/bruno-m-santos/lt')
        self.env = EnvironmentVarGuard()
        self.env.set('MONGODB_HOST', 'localhost')
        self.env.set('MONGODB_DATABSE', 'gitbase')

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual(b'lt', self.response.data)


if __name__ == '__main__':
    unittest.main()
