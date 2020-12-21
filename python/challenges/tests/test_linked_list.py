from challenges.linked_list.linked_list import LinkedList, Node

link = LinkedList()

def test_empty_list():
    actual = link.insert(Node(None))
    value = None
    assert actual == value

def test_insert_list_with_value_5():
    actual = link.insert(Node(5))
    value = None
    assert actual == value

def test_head_link():
    actual = str(link)
    value = '{5} -> {None} -> NULL'
    assert actual == value

new_link = LinkedList()

def test_multiple_insert():
    new_link.insert(Node('c'))
    new_link.insert(Node('b'))
    new_link.insert(Node('a'))
    actual = str(new_link)
    value = "{'a'} -> {'b'} -> {'c'} -> NULL"
    assert actual == value

def test_find_value():
    actual = new_link.includes('c')
    value = True
    assert actual == value

def test_false_includes():
    actual = new_link.includes('h')
    value = False
    assert actual == value

def test_collection():
    actual = str(new_link)
    value = "{'a'} -> {'b'} -> {'c'} -> NULL"
    assert actual == value
