import pytest
from challenges.fizz_buzz_tree.fizz_buzz_tree import Node, Binary_Tree, fizz_buzz_tree

def test_empty_tree():
    t = Binary_Tree(Node())
    actual = fizz_buzz_tree(t)
    expected = None
    assert actual == expected

def test_tree_input():
    t = Binary_Tree(Node(1))
    t.root.left = Node(4)
    t.root.right = Node(9)
    t.root.left.left = Node(15)
    t.root.left.right = Node(26)
    t.root.right.left = Node(20)
    actual = fizz_buzz_tree(t)
    expected = [1, 4, 'FizzBuzz', 26, 'Fizz', 'Buzz']
    assert actual == expected
