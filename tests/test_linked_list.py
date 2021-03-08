import unittest

from src.ch2.linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):

    def test_linked_list(self):
        l = LinkedList()

        self.assertEqual(l.head, None)


    def test_linked_list_add(self):
        l = LinkedList()

        l.add(1)
        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next, None)

        l.add(2)
        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)

    
    def test_get(self):
        l = LinkedList()

        l.add(1)
        self.assertEqual(l.get(0).data, 1)

        l.add(2)
        self.assertEqual(l.get(1).data, 2)


    def test_remove(self):
        l = LinkedList()

        l.remove(0)
        self.assertEqual(l.head, None)

        l.add(1)
        l.remove(0)
        self.assertEqual(l.head, None)

        l = LinkedList()

        l.add(1)
        l.add(2)
        l.remove(1)
        self.assertEqual(l.head.next, None)

        l = LinkedList()

        l.add(1)
        l.add(2)
        l.add(3)
        l.remove(2)
        self.assertEqual(l.head.data, 1)
        self.assertEqual(l.head.next.data, 2)
        self.assertEqual(l.head.next.next, None)
