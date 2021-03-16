from linked_list import LinkedList, Node

class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self._bucket = size * [None]

    # single underscore means it's a private method
    def _hash(self,key):
        total = 0
        for char in key:
            total += ord(char)
        primed = total * 17
        index = primed % self.size
        return index

    def add(self, key, value):
        hashed_key_index = self._hash(key)
        if not self._bucket[hashed_key_index]:
            self._bucket[hashed_key_index] = LinkedList()
        self._bucket[hashed_key_index].insert((key, value))

    def get(self, requested_key):
        hashed_key_index = self._hash(requested_key)
        temp = self._bucket[hashed_key_index]
        if temp is None:
            return
        while temp.head is not None:
            current = temp.head
            if current.value[0] == requested_key:
                return current.value[1]
            current = current.next   

    def contains(self, requested_key):
        hashed_key_index = self._hash(requested_key)
        temp = self._bucket[hashed_key_index]
        found = False
        if temp is None:
            return found
        while temp.head is not None:
            current = temp.head
            if current.value[0] == requested_key:
                found = True
                return found
            current = current.next
        return found

if __name__ == "__main__":
    test_hash = HashTable()
    test_hash.set('clam', 'bagel')
    test_hash.set('calm', '5')
    # print(test_hash.get('clam'))
    print(test_hash.get('calm'))

