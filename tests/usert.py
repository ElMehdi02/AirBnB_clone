#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_initialization(self):
        """Test object initialization."""
        # Create an instance of User
        user = User()

        # Assert that the id, created_at, and updated_at attributes are set
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    # Add more test methods as needed
