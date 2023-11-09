#!/usr/bin/python3

import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = Review()
        self.u_id = User()
        self.p_id = Place()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.place_id, "")
        self.assertEqual(self.new_user.user_id, "")
        slef.assertEqual(self.new_user.text, "")

    def test_user_attribute(self):
        self.new_user.place_id = self.p_id.id
        self.new_user.user_id = self.u_id.id
        self.new_user.text = "Hello world"

        self.assertEqual(self.new_user.place_id, self.p_id.id)
        self.assertEqual(self.new_user.user_id, self.u_id.id)
        self.assertequal(self.new_user.text, "Hello world")


if __name__ == '__main__':
    unittest.main()
