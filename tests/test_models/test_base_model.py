#!/usr/bin/python3
""" Unittest for the base model module.

Unittests is collection of all possible edge cases on
which this module shouldnt be expected to fail, and cases
on which is expected to fail.

"""
from models.base_model import BaseModel
from datetime import timedelta
import unittest

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class in the base_model module.

    """

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_kwargs(self):
        id = str(uuid.uuid4())
        created_at = datetime.now() - timedelta(days=1)
        updated_at = datetime.now() - timedelta(hours=1)
        model = BaseModel(id=id, created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.id, id)
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['__class__'], str)

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIsInInstance(model_str, str)
        self.assertgreater(len(model_str), 0)
        self.assertIn('[', model_str)
        self.assertIn(']', model_str)
        self.assertIn('(', model_str)
        self.assertIn(')', model_str)
        self.assertIn('{', model_str)
        self.assertIn('}', model_str)
        self.assertIn('id', model_str)
        self.assertIn('created_at', model_str)
        self.assertIn('updated_at', model_str)

if __name__ == '__main__':
    unittest.main()
