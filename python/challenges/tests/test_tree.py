import pytest
from challenges.tree.tree import Node, BinaryTree

def test_empty_tree():
    t = BinaryTree(Node())
    actual = t.root.value
    expected = None
    assert actual == expected

def test_one_root_on_tree():
    t = BinaryTree(Node("A"))
    actual = t.root.value
    expected = "A"
    assert actual == expected 

def test_add_left_and_right_node():
    pass

def test_pre_order_traversal():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    tree = BinaryTree(Node("A"))
    tree.root.left = b
    tree.root.right = c
    tree.root.left.left = d
    tree.root.left.right = e
    tree.root.right.left = f
    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == expected 

def test_in_order_traversal():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    tree = BinaryTree(Node("A"))
    tree.root.left = b
    tree.root.right = c
    tree.root.left.left = d
    tree.root.left.right = e
    tree.root.right.left = f
    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == expected 


def test_post_order_traversal():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    tree = BinaryTree(Node("A"))
    tree.root.left = b
    tree.root.right = c
    tree.root.left.left = d
    tree.root.left.right = e
    tree.root.right.left = f
    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected 

def test_instantiate_tree():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    actual = tree.find_maximum_value()
    expected = 11
    assert actual == expected