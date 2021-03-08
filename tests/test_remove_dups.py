import unittest

from src.ch2.remove_dups import remove_dups
from src.ch2.linked_list import LinkedList


class RemoveDupsTestCase(unittest.TestCase):

    def test_remove_dups(self):
        l = LinkedList()
        self.assertEqual(remove_dups(l), None)
        self.assertEqual(l.len(), 0)

        l = LinkedList()
        l.add(1)
        l.add(1)

        remove_dups(l)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next, None)
        self.assertEqual(l.len(), 1)

        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(2)

        remove_dups(l)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next, None)
        self.assertEqual(l.len(), 2)

        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(2)
        l.add(3)

        remove_dups(l)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next.data, 3)
        self.assertEqual(l.len(), 3)

        l = LinkedList()
        l.add(1)
        l.add(2)
        l.add(1)
        l.add(3)

        remove_dups(l)

        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next.data, 3)
        self.assertEqual(l.len(), 3)
