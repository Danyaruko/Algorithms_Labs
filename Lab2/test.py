import unittest
from stack import Stack
from stack import Node


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(3)
        self.stack.push(5)
        self.stack.push(7)

    def test_peek(self):
        self.assertEqual(self.stack.peek(),  7)

    def test_push(self):
        self.stack.push(11)
        self.assertMultiLineEqual(f"The top element of the stack is: {self.stack.peek()}", "The top element of the stack is: 11")

    def test_pop(self):
        self.stack.pop
        self.assertMultiLineEqual(f"The top element of the stack is: {self.stack.peek()}", "The top element of the stack is: 7")

    def test_search(self):
        self.assertTupleEqual(self.stack.search(5), (5, 2))