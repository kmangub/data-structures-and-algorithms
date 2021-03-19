import pytest
from challenges.tree_intersection.tree_intersection import tree_intersection, Node, BinaryTree

def test_empty_tree_intersect_with_tree_with_one_node():
    t = BinaryTree()
    t2 = BinaryTree(Node('A'))
    actual = tree_intersection(t,t2)
    expected = []
    assert actual == expected

def test_tree_intersect_with_tree_with_tree():
    t = BinaryTree(Node("A"))
    t.root.left = Node("B")
    t.root.right = Node("C")
    t.root.left.left = Node("D")
    t.root.left.right = Node("E")
    t.root.right.left = Node("F")

    t2 = BinaryTree(Node('B'))
    t2.root.left = Node("B")
    t2.root.right = Node("C")
    t2.root.left.left = Node("D")
    t2.root.left.right = Node("E")
    t2.root.right.left = Node("F")

    actual = tree_intersection(t,t2)
    expected = ['B', 'D', 'E', 'C', 'F']
    assert actual == expected

def test_tree_intersect_with_tree_with_tree():
    t = BinaryTree(Node(26))
    t.root.left = Node(1)
    t.root.right = Node(17)
    t.root.left.left = Node(5)
    t.root.left.right = Node(5)
    t.root.right.left = Node(12)

    t2 = BinaryTree(Node('B'))
    t2.root.left = Node(12)
    t2.root.right = Node(12)
    t2.root.left.left = Node("D")
    t2.root.left.right = Node(1)
    t2.root.right.left = Node("F")

    actual = tree_intersection(t,t2)
    expected = [1,12]
    assert actual == expected
