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
    def __init__(self):
        self.head = None
    
    def insert(self, node):
        node.next = self.head
        self.head = node

    def includes(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

    def __str__(self):
        temp = self.head
        string = ''
        node_list = [] 
        while(temp): 
            node_list.append(f"{ {temp.data} } -> ")
            temp = temp.next
            if temp == None:
              node_list.append('NULL')
        for node in node_list:
          string += f'{node}'
        return string

class Node:
    """
    Initializes Node class with data and next as none.

    getData contains the value of the node

    get next will look at the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next



