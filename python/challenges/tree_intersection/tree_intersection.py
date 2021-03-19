class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right 

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

def tree_intersection(tree1,tree2):
    intersection = []
    list_tree_1 = []
    list_tree_2 = []

    if tree1.root is None:
        return list_tree_1
    else:
        def traverse1(root):
            list_tree_1.append(root.value)
            if root.left:
                traverse1(root.left)
            if root.right:
                traverse1(root.right)
        
        traverse1(tree1.root)

    if tree2.root is None:
        return list_tree_2
    else:
        def traverse2(root):
            list_tree_2.append(root.value)
            if root.left:
                traverse2(root.left)
            if root.right:
                traverse2(root.right)

        traverse2(tree2.root)

    for item in list_tree_1:
        if item in list_tree_2:
            intersection.append(item)
    return intersection


    
if __name__ == "__main__":
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

    tree2 = BinaryTree(Node("A"))
    tree2.root.left = b
    tree2.root.right = c
    tree2.root.left.left = d
    tree2.root.left.right = e
    tree2.root.right.left = f

    tree3 = BinaryTree(Node('C'))
    tree3.root.left = Node(3)
    # print(tree_intersection(tree,tree2))
    # print(tree2.root.left.left.value)
    # print(traverse(tree2.root))

    print(tree_intersection(tree3,tree2))