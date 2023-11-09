#!/usr/bin/python3

import unittest
from models.state import State


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = State()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.name, "")

    def test_user_attribute(self):
        self.new_user.name = "Betty"

        self.assertEqual(self.new_user.name, "Betty")


if __name__ == '__main__':
    unittest.main()
