"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node
from src.stack import Stack


class TestNode(unittest.TestCase):
    def test_data(self):
        self.assertEqual(Node(3, None).data, 3)
        self.assertEqual(Node(4, 2).next_node, 2)


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push("Lilo")
        stack.push("Stitch")
        self.assertEqual(stack.top.data, "Stitch")
        self.assertEqual(stack.top.next_node.data, "Lilo")
        self.assertEqual(stack.top.next_node.next_node, None)





