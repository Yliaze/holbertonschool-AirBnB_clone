#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()

    def test_init(self):
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.id, str)

    def test_str(self):
        model_str = "[{}] ({}) {}".format(self.my_model.__class__.__name__,
                                          self.my_model.id, 
                                          self.my_model.__dict__)
        self.assertEqual(str(self.my_model), model_str)

    def test_save(self):
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict["created_at"], self.my_model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.my_model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], self.my_model.__class__.__name__)
        self.assertEqual(model_dict["id"], self.my_model.id)

if __name__ == "__main__":
    unittest.main()
