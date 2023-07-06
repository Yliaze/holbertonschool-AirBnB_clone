#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.my_model = BaseModel()
        self.storage.new(self.my_model)

    def test_all(self):
        all_objects = self.storage.all()
        key = "{}.{}".format(type(self.my_model).__name__, self.my_model.id)
        self.assertIn(key, all_objects.keys())

    def test_new(self):
        key = "{}.{}".format(type(self.my_model).__name__, self.my_model.id)
        self.assertIn(key, self.storage.all().keys())


if __name__ == "__main__":
    unittest.main()
