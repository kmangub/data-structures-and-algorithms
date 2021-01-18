# from challenges.stacks_and_queues.stacks_and_queues import Queue, Node, InvalidOperationError

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
            output += f'{{ {current.value} }} -> '
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
        return False

class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, value):
        """
        This method takes in a value and untilizes the FIFO approach
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        This method will check to see if the stack is empty, then it will return the 
        top 
        """
        while self.stack1.peek():
            if self.stack1.top.next == None:
                return self.stack1.top.value

            else:
                temp = self.stack1.pop()
                self.stack2.push(temp)
                continue
                
if __name__ == "__main__":
    new_stack = Stack()
    new_stack.push("10")
    new_stack.push("15")
    new_stack.push("20")
    # new_stack.pop()
    # new_stack.pop()
    print(new_stack)
        
    
        
        