#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = Amenity()

    def teardown(self):
        del self.new_user

    def test_user_type(self):
        self.asserEqual(self.new_user.name, "")

    def test_user_attribute(self):
        self.new_user.name = "Root"

        self.asserEqual(self.new_user.name, "Root")


if __name__ = '_main__':
    unittest.main()
