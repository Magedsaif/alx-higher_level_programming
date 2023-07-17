import unittest
from models.base import Base
"""Test_Base"""


class test_Base(unittest.TestCase):
    """Class test_Base"""

    def test_init(self):
        a = Base()
        self.assertEqual(a.id, 1)

        a1 = Base()
        self.assertEqual(a1.id, 2)

        a2 = Base(12)
        self.assertEqual(a2.id, 12)
