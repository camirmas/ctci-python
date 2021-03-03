import unittest

from src.ch1.check_permutations import check_permutations


class CheckPermutationsTestCase(unittest.TestCase):

    def test_check_permutations(self):
        self.assertTrue(check_permutations("act", "cat"))


    def test_check_permutations_false(self):
        self.assertFalse(check_permutations("acta", "catb"))
