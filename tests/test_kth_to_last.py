import unittest

from src.ch2.kth_to_last import kth_to_last
from src.ch2.linked_list import LinkedList


class KthToLastTestCase(unittest.TestCase):

    def test_kth_to_last(self):
        l = LinkedList()
        l.add(1)
        self.assertEqual(kth_to_last(l, 1), l.head)

        l.add(2)
        self.assertEqual(kth_to_last(l, 2), l.head)

        l.add(2)
        self.assertEqual(kth_to_last(l, 2).data, 2)
        self.assertEqual(kth_to_last(l, 3), l.head)
