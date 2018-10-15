import unittest
from main import app as my_app


class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = my_app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
