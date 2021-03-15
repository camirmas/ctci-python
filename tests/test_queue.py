import unittest

from src.ch3.queue import Queue


class QueueTestCase(unittest.TestCase):

    def test_is_empty(self):
        self.assertTrue(Queue().is_empty())

    
    def test_add(self):
        q = Queue()
        q.add(2)

        self.assertFalse(q.is_empty())
        self.assertEqual(q.first.data, 2)


    def test_remove(self):
        q = Queue()
        q.add(2)
        q.add(3)

        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertTrue(q.is_empty())


    def test_peek(self):
        q = Queue()
        q.add(2)
        q.add(3)

        self.assertEqual(q.peek(), 2)
