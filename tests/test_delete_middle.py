import unittest

from src.ch2.delete_middle import delete_middle
from src.ch2.linked_list import LinkedList


class DeleteMiddleTestCase(unittest.TestCase):
    
    def test_delete_middle(self):
        l = LinkedList()

        l.add(1)
        l.add(2)
        l.add(3)

        delete_middle(l.head.next)

        self.assertEqual(l.len(), 2)
        self.assertEqual(l.head.next.data, 3)

        l = LinkedList()

        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)

        delete_middle(l.head.next.next)
        self.assertEqual(l.len(), 3)
        self.assertEqual(l.head.next.next.data, 4)
