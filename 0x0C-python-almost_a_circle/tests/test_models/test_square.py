"""Unittesting for the Square module/class
Tests are done for each method of the class"""
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassSquare(unittest.TestCase):
    """Test class for testing Square class"""
    def test_pep8_base(self):
        """
        Test that models/square.py is pep8 compliant.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors,
                         0, "Found code style errors (and warnings).")

    def tearDown(self):
        """
        Reset the Base._nb_objects to 0
        """
        Base._nb_objects = 0

    def test_width(self):
        """
        Test that the width of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        s2 = Square(10, 0, 0, 12)

    def test_width_type(self):
        """
        Test that the width of the square is of type int
        """
        s1 = Square(10)
        self.assertEqual(type(s1.width), int)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(type(s2.width), int)

    def test_height(self):
        """
        Test that the height of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.height, 10)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(s2.height, 10)

    def test_height_type(self):
        """
        Test that the height of the square is of type int
        """
        s1 = Square(10)
        self.assertEqual(type(s1.height), int)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(type(s2.height), int)

    def test_raise_size_x_y(self):
        """
        Test that the height of the square is correct
        """
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1 = Square("10")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            s2 = Square(10, "0")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            s3 = Square(10, 0, "0")

    def test_x(self):
        """
        Test that the x of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.x, 0)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(s2.x, 0)

    def test_size_area(self):
        """
        Test that tests use of size method and area
        """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.area(), 100)
        s1 = Square(2, 8)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.area(), 4)
        s1 = Square(3, 1, 3)
        self.assertEqual(s1.size, 3)
        with self.assertRaises(ValueError, msg="height must be an integer"):
            s1 = Square(-10)


class NewTest(unittest.TestCase):
    def test_id(self):
        """
        Test that the id of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(s2.id, 12)


if __name__ == "__main__":
    unittest.main()
