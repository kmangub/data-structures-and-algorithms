class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right 

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
    
    def pre_order(self):
        pre_order_list = []
        def traverse(root):
            pre_order_list.append(root.value)
            if root.left: 
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return pre_order_list
    
    def in_order(self):
        in_order_list = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            in_order_list.append(root.value)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return in_order_list
    
    def post_order(self):
        post_order_list = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            post_order_list.append(root.value)
        traverse(self.root)
        return post_order_list
    
    def find_maximum_value(self):
        max_value = 0
        def traverse(root):
            nonlocal max_value
            if root.value > max_value:
                max_value = root.value
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return max_value



class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_node = Node(value)
        def traverse(node):
            if new_node.value < node.value:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = new_node
            else:       
                if node.right:
                    traverse(node.right)
                else:
                    node.right = new_node
        if self.root is None:
            self.root = new_node
        else:    
            traverse(self.root)    

if __name__ == "__main__":
    # a = Node("A")
    # b = Node("B")
    # c = Node("C")
    # d = Node("D")
    # e = Node("E")
    # f = Node("F")
    # tree = BinaryTree(Node("A"))
    # tree.root.left = b
    # tree.root.right = c
    # tree.root.left.left = d
    # tree.root.left.right = e
    # tree.root.right.left = f
    # print(tree.in_order())
    # print(tree.pre_order())
    # print(a.value)
    # print(tree.post_order())
    # tree2 = BinarySearchTree()
    # tree2.add(3)
    # tree2.add(4)
    # tree2.add(30)
    # tree2.add(25)
    # print(tree2.root.value)
    # print(tree2.root.right.value)
    # print(tree2.root.right.right.value)
    # print(tree2.root.right.right.left.value)

    max_tree = BinaryTree(Node(600))
    max_tree.root.left = Node(500)
    max_tree.root.right = Node(300)
    max_tree.root.left.left = Node(400)
    max_tree.root.left.right = Node(100)
    max_tree.root.right.left = Node(200)
    print(max_tree.find_maximum_value())
    # print(max_tree.pre_order())