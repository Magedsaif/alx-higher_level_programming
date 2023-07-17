import unittest
from models.rectangle import Rectangle
"""Test_Recatngle"""


class test_Rectangle(unittest.TestCase):
    """Class test_recatngle"""

    def test_init(self):

        a = Rectangle(10, 12)
        self.assertEqual(a.id, 1)

        a1 = Rectangle(10, 12, 0, 0, 12)
        self.assertEqual(a1.id, 12)

        with self.assertRaises(TypeError) as error:
            Rectangle("a", 10)
        self.assertEqual(str(error.exception), "width must be an integer")

        with self.assertRaises(ValueError) as error:
            Rectangle(-1, 10)
        self.assertEqual(str(error.exception), "width must be > 0")

        with self.assertRaises(TypeError) as error:
            x = Rectangle(9, 10)
            x.width = "a"
        self.assertEqual(str(error.exception), "width must be an integer")

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
