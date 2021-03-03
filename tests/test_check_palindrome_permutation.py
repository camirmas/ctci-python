import unittest

from src.ch1.check_palindrome_permutation import check_palindrome_permutation


class CheckPalindromePermutationTestCase(unittest.TestCase):

    def test_check_palindrome_permutation(self):
        self.assertTrue(check_palindrome_permutation("tactcoa"))


    def test_check_palindrome_permutation_2(self):
        self.assertTrue(check_palindrome_permutation("amanaplanacanalpanama"))


    def test_check_palindrome_permutation_false(self):
        self.assertFalse(check_palindrome_permutation("amanaplanacanalpanamas"))
