from challenges.hashtable.hashtable import HashTable

def test_create():
    hashtable = HashTable()
    assert hashtable

def test_predictable_hash():
    hashtable = HashTable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary

def test_in_range_hash():
    hashtable = HashTable()
    actual = hashtable._hash('spam')
    # assert actual >= 0
    # assert actual < hashtable.size
    assert 0 <= actual < hashtable.size

def test_same_hash():
    hashtable = HashTable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary

def test_different_hash():
    hashtable = HashTable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary

def test_get_add():
    hashtable = HashTable()
    hashtable.add('cat','dog')
    actual = hashtable.get('cat')
    expected = 'dog'
    assert actual == expected

def test_contains():
    hashtable = HashTable()
    hashtable.add('cat','dog')
    actual = hashtable.contains('cat')
    expected = True
    assert actual == expected