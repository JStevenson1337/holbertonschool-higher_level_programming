#!/usr/bin/python3
"""
Test for Base Class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)


if __name__ == "__main__":
    unittest.main()
