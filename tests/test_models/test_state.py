#!/usr/bin/python3
"""Unittests for models/state.py.
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing the init of the State class."""
    def test_no_arguments_init(self):
        self.assertEqual(State, type(State()))

    def test_instance_stored(self):
        self.assertIn(State(), models.storage.all().values())

    def test_is_id_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_is_created_at_public_(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_is_updated_at_public_(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public(self):
        am = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(State()))
        self.assertNotIn("name", am.__dict__)

    def test_unique_ids(self):
        am1 = State()
        am2 = State()
        self.assertNotEqual(am1.id, am2.id)

    def test_created_at(self):
        am1 = State()
        sleep(0.1)
        am2 = State()
        self.assertLess(am1.created_at, am2.created_at)

    def test_updated_at(self):
        am1 = State()
        sleep(0.1)
        am2 = State()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        m = State()
        m.id = "54321"
        m.created_at = m.updated_at = dt
        amstr = m.__str__()
        self.assertIn("[State] (54321)", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'id': '54321'", amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        m = State(None)
        self.assertNotIn(None, m.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        m = State(id="543", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(m.id, "543")
        self.assertEqual(m.created_at, dt)
        self.assertEqual(m.updated_at, dt)

    def test_instantiation_with_None(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_added_attributes(self):
        m = State()
        m.middle_name = "Umegain"
        m.my_number = 56
        self.assertEqual("Umegain", m.middle_name)
        self.assertIn("my_number", m.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        m = State()
        m_dict = m.to_dict()
        self.assertEqual(str, type(m_dict["id"]))
        self.assertEqual(str, type(m_dict["created_at"]))
        self.assertEqual(str, type(m_dict["updated_at"]))

    def test_to_dict_out(self):
        dt = datetime.today()
        m = State()
        m.id = "654321"
        m.created_at = m.updated_at = dt
        tdict = {
            'id': '654321',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(m.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()
