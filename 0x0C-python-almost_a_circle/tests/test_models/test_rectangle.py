#!/usr/bin/python3
"""Unittesting for the Rectangle module/class
Tests are done for each method of the class"""


import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassRectangle(unittest.TestCase):
    """Test class for testing Rectangle class"""
    def test_pep8_rectangle(self):
            """
            Test that models/rectanlge.py is pep8 compliant.
            """
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/rectangle.py'])
            self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")
# these tests worked locally
    def setUp(self):
        self.inst = Rectangle(1, 2, 3, 4, 5)

    def test_width(self):
        """
        test rectangle height
        """
        self.assertEqual(self.inst.width, 1)

    def test_width(self):
        """
        test rectangle width
        """
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """
        text x
        """
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.inst.y, 4)
