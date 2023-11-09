#!/usr/bin/python3
"""Unittest for the FileStorage class"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for all methods in the FileStorage class"""

    def setUp(self):
        """Setting up the test cases"""
        super().setUp()
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self._objs = storage._FileStorage__objects
        self.keyname = "BaseModel." + self.instance.id

    def tearDown(self):
        """Cleaning the file path"""
        super().tearDown()
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_methods(self):
        obj = FileStorage
        self.assertTrue(hasattr(obj, "all"))
        self.assertTrue(hasattr(obj, "new"))
        self.assertTrue(hasattr(obj, "save"))
        self.assertTrue(hasattr(obj, "reload"))

    def test_all_method(self):
        """Test the all() method"""
        result = storage.all()
        self.assertEqual(result, self._objs)

    def test_new_method(self):
        """Test the new() method"""
        storage.new(self.instance)
        key = f"{self.instance.__class__.__name__}.{self.instance.id}"
        self.assertIn(key, self._objs)

    def test_save_method(self):
        """Test the save() method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()
        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)

        expected_data = {}
        for key, value in self._objs.items():
            expected_data[key] = value.to_dict()

        self.assertEqual(saved_data, expected_data)

    def test_reload_method(self):
        """Test the reload() method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        storage.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self._objs = {}
        self.assertEqual(reloaded_data[self.keyname], saved_data[self.keyname])

    def test_path(self):
        """Test the existence of the JSON file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        storage.reload()


if __name__ == "__main__":
    unittest.main()
