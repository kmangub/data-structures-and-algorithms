class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right 

class Binary_Tree:
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        pre_order_list = []

        def traverse(root):

            if root is None:
                return
            
            pre_order_list.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return pre_order_list


def fizz_buzz_tree(tree):
    root = tree.root
    fizz_buzz_tree_list = []
    if root.value is None:
            return
    def traverse(root):
        if root is None:
            return
        if root.value % 3 == 0 and root.value % 5 == 0: 
            root.value = 'FizzBuzz'
        elif root.value % 3 == 0:
            root.value = 'Fizz'
        elif root.value % 5 == 0:
            root.value = 'Buzz'
        # else:
        fizz_buzz_tree_list.append(root.value)
        traverse(root.left)
        traverse(root.right)
    traverse(root)

    return fizz_buzz_tree_list

if __name__ == "__main__":
    normal_tree = Binary_Tree(Node(1))
    normal_tree.root.left = Node(4)
    normal_tree.root.right = Node(9)
    normal_tree.root.left.left = Node(15)
    normal_tree.root.left.right = Node(26)
    normal_tree.root.right.left = Node(20)

    # print(normal_tree.pre_order())
    # print(fizz_buzz_tree(normal_tree))


    t = Binary_Tree(Node())
    print(fizz_buzz_tree(t))
