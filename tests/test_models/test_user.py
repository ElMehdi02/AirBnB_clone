#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.email, "")
        self.assertEqual(self.new_user.password, "")
        self.assertEqual(self.new_user.first_name, "")
        self.assertEqual(self.new_user.last_name, "")

    def test_user_attribute(self):
        self.new_user.first_name = "Betty"
        self.new_user.last_name = "Bar"
        self.new_user.email = "airbnb@mail.com"
        self.new_user.password = "root"

        self.assertEqual(self.new_user.email, "airbnb@mail.com")
        self.assertEqual(self.new_user.first_name, "Betty")
        self.assertEqual(self.new_user.last_name, "Bar")
        self.assertEqual(self.new_user.password, "root")


if __name__ == '__main__':
    unittest.main()
