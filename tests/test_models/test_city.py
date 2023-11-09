#!/usr/bin/python3

import unittest
from models.city import City
from models.state import State


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = City()
        self.s_id = State()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.state_id, "")
        self.assertEqual(self.new_user.name, "")

    def test_user_attribute(self):
        self.new_user.name = "Root"
        self.new_user.state_id = self.s_id.id

        self.assertEqual(self.new_user.name, "Root")
        self.assertEqual(self.new_user.state_id, self.s_id.id)


if __name__ == '__main__':
    unittest.main()
