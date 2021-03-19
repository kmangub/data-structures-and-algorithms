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
    list_tree_1 = pre_order(tree1)
    list_tree_2 = pre_order(tree2)
    
    for i in range(len(list_tree_1)):
        if list_tree_1[i] in list_tree_2:
            intersection.append(list_tree_1[i])
            list_tree_2.remove(list_tree_1[i])
    return intersection

def pre_order(tree):
        pre_order_list = []
        if tree.root is None:
            return []
        def traverse(root):
            pre_order_list.append(root.value)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(tree.root)
        return pre_order_list
        
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
    # a = [1,1,2]
    # b = [1,2]
    # c = []
    # for i in range(len(a)):
        # print(i)
        # print(a[i])
        # if a[i] in b:
        #     c.append(a[i])
        #     b.remove(a[i])
    # print(a)
    # print(b)
    # print(c)
    print(tree_intersection(tree3,tree2))