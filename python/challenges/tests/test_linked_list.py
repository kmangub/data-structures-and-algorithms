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
    link_3 = LinkedList()
    link_3.insert(5)
    actual = str(link_3)
    expected = '{ 5 } -> None'
    assert actual == expected

new_link = LinkedList()

def test_multiple_insert():
    new_link.insert('c')
    new_link.insert('b')
    new_link.insert('a')
    actual = str(new_link)
    value = "{ a } -> { b } -> { c } -> None"
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
    value = "{ a } -> { b } -> { c } -> None"
    assert actual == value
