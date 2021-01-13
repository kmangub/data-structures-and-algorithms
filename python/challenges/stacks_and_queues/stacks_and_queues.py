class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack():
    def __init__(self, node = None):
        self.top = node

    def __str__(self):
        # { a } -> { b } -> { c } -> NULL

        output = ''
        current = self.top
    
        while current is not None:
            output += f'{{ {current.value} }} -> None'
            current = current.next
        return output
    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top 
        self.top = self.top.next
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")        
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
        

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        # { a } -> { b } -> { c } -> NULL

        output = ''
        current = self.front
    
        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output

    def enqueue(self, value):
        node = Node(value)
        node.next = self.front
        self.rear = node
    
    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")        
        return self.front.value

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

if __name__ == "__main__":
    # new_stack.push("apple")
    # new_stack.push("banana")
    # new_stack.push("cucumber")
    # new_stack.pop()
    # new_stack.pop()
    # print(new_stack)
    # print(new_stack.is_empty())
    
    new_queue = Queue()
    new_queue.enqueue("apple")
    new_queue.enqueue("banana")
    new_queue.enqueue("cucumber")
    print(new_queue)