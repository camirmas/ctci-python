import unittest

from src.ch1.compress_string import compress_string


class CompressStringTestCase(unittest.TestCase):

    def test_compress_string(self):
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("a"), "a1")
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
