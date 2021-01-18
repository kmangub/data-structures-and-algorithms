
class Node:
    """
    Initializes Node class with data and next as none.

    getData contains the value of the node

    get next will look at the next node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Initializes with head of none

    insert method which takes any value as 
    an argument and adds a new node with that 
    value to the head.

    includes method takes in a value as an
    argument, assigns current as head, and
    returns a boolean.

    str method puts nodes in a string and end
    with NULL.
    """
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        # { a } -> { b } -> { c } -> NULL

        output = ''
        current = self.head
    
        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + 'None'
    
    def insert(self, value):
        node = Node(value)
        
        if self.head is not None:
            node.next = self.head

        self.head = node 

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        
        return False

    # def function(self, some_list):
    #     current = self.head
    #     new_linked = LinkedList()

    #     while current is not None:
    #         for value in some_list:
    #             node = Node(value)
    #             value = current.next 
    #             current = current.next
    #             self.head = node
        
    #     return new_linked

         


if __name__ == "__main__":
    new_linked = LinkedList()
    new_linked.insert(5)
    print(new_linked)
