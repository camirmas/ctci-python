import unittest

from src.ch1.one_away import one_away


class OneAwayTestCase(unittest.TestCase):

    def test_one_away(self):
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("ple", "pale"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "pales"))
        self.assertTrue(one_away("pale", "bale"))
        self.assertTrue(one_away("bale", "pale"))
        self.assertTrue(one_away("", ""))
        self.assertTrue(one_away("s", ""))
        self.assertTrue(one_away("", "s"))
        self.assertTrue(one_away("ppp", "pp"))
        self.assertTrue(one_away("pp", "ppp"))
        self.assertFalse(one_away("", "aa"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("pale", ""))
        self.assertFalse(one_away("pale", "p"))
        self.assertFalse(one_away("pppp", "pp"))
        self.assertFalse(one_away("pp", "pppp"))
        self.assertFalse(one_away("ppaa", "pa"))
