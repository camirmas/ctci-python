import unittest
from src.ch1.is_unique import is_unique


class IsUniqueTestCase(unittest.TestCase):

    def test_is_unique(self):
        self.assertTrue(is_unique("cat"))


    def test_is_unique_false(self):
        self.assertFalse(is_unique("appa"))
