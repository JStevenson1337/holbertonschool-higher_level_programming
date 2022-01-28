#!/usr/bin/python3
"""Unittesting for the Base module/class
Tests are done for each method of the class"""


import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassBase(unittest.TestCase):
    """Test class for testing Base class"""

    def test_pep8_base(self):
            """
            Test that models/base.py is pep8 compliant.
            """
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/base.py'])
            self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """
        Test that tests/test_models/test_base.py is pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests docstrings functions
        """
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

class NewTest(unittest.TestCase):
    def test_id_sets(self):
        """ 
        Tests no passed ID
        Passed id
        then no passed ID again
        """
        b1 = Base()
        b98 = Base(98)
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b98.id, 98)
        self.assertEqual(b2.id, 2)

    def test_too_many_args(self):
        """
        test too many args to init
        """
        with self.assertRaises(TypeError):
            b = Base(1, 1)
