class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __str__(self):
        # FRONT -> { a } -> { b } -> { c } -> { d } REAR
        if self.front == None:
            return "NULL"
        output = 'FRONT -> '
        front = self.front
        rear = self.rear
    
        while front:
            output += f'{front.value} -> '
            front = front.next
        output += 'REAR'
        return output

    def enqueue(self, animal):
        animal = animal.lower()
        node = Node(animal)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def dequeue(self, pref):
        pref = pref.lower()
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        if pref == "cat" or pref == 'dog':
            node = self.front
            self.front = self.front.next
            return node.value
        else:
            return "null"
    
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

# if __name__ == "__main__":
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("cat")
#     a.dequeue("cat")
#     print(a)