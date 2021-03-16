import unittest

from src.ch3.stack_min import Stack


class StackTestCase(unittest.TestCase):

    def test_is_empty(self):
        self.assertTrue(Stack().is_empty())


    def test_push(self):
        stack = Stack()
        stack.push(3)

        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.top.data, 3)


    def test_pop(self):
        stack = Stack()
        stack.push(3)

        self.assertEqual(stack.pop() , 3)
        self.assertTrue(stack.is_empty())

    
    def test_peek(self):
        stack = Stack()
        stack.push(3)

        self.assertEqual(stack.peek(), 3)
        self.assertFalse(stack.is_empty())


    def test_min(self):
        stack = Stack()
        stack.push(3)

        self.assertEqual(stack.min(), 3)
        stack.push(2)
        self.assertEqual(stack.min(), 2)
        stack.push(4)
        self.assertEqual(stack.min(), 2)
        stack.push(1)
        self.assertEqual(stack.min(), 1)
