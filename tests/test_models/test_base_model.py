#!/usr/bin/python3
"""Defines unittests for models/base_model.py
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_initialization(unittest.TestCase):
    """Unittests for testing the init method of the BaseModel class."""
    def test_no_arguments_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_instance_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_is_id_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_is_created_at_public_(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_is_updated_at_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_unique(self):
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)

    def test_models_created_at(self):
        m1 = BaseModel()
        sleep(0.1)
        m2 = BaseModel()
        self.assertLess(m1.created_at, m2.created_at)

    def test_models_updated_at(self):
        m1 = BaseModel()
        sleep(0.1)
        m2 = BaseModel()
        self.assertLess(m1.updated_at, m2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "54321"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("'updated_at': " + dt_repr, bmstr)
        self.assertIn("'id': '54321'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("[BaseModel] (54321)", bmstr)

    def test_args_not_used(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        m = BaseModel(id="765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(m.id, "765")
        self.assertEqual(m.created_at, dt)
        self.assertEqual(m.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("27", id="765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "765")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


if __name__ == "__main__":
    unittest.main()
