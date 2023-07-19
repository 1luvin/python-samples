import unittest

from stack import Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        self.emptyStack = Stack()

        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.filledStack = stack

        stack = Stack(size=2)
        stack.push(1)
        stack.push(2)
        self.fullStack = stack

    def test_is_empty(self):
        self.assertEqual(self.emptyStack.is_empty(), True)
        self.assertEqual(self.filledStack.is_empty(), False)
        self.assertEqual(self.fullStack.is_empty(), False)

    def test_is_full(self):
        self.assertEqual(self.emptyStack.is_full(), False)
        self.assertEqual(self.filledStack.is_full(), False)
        self.assertEqual(self.fullStack.is_full(), True)

    def test_push(self):
        stack = Stack(size=2)
        self.assertEqual(str(stack), '[]')
        stack.push(1)
        self.assertEqual(str(stack), '[1]')
        stack.push(2)
        self.assertEqual(str(stack), '[1, 2]')
        with self.assertRaises(ValueError):
            stack.push(3)

    def test_pop(self):
        stack = self.filledStack
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        with self.assertRaises(ValueError):
            stack.pop()
