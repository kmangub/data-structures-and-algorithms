from challenges.array_binary_search import __version__

from challenges.array_binary_search.array_binary_search import binary_search

def test_version():
    assert __version__ == '0.1.0'

def test_number_contained_inside_list():
    actual = binary_search([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected

def test_number_not_contained_inside_list():
    actual = binary_search([11,22,33,44,55,66,77], 88)
    expected = -1
    assert actual == expected


