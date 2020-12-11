from array_shift import __version__
from array_shift.array_shift import array_length, insert_number

def test_version():
    assert __version__ == '0.1.0'


def test_array_length():
    actual = array_length([3,4,5,6,7])
    expected = 5
    assert actual == expected

# def test_midpoint():
#     actual = midpoint( 2 % array_length(temp))
#     expected = 1
#     assert actual == expected

def test_insertion():
    actual = insert_number([3,4,5,6,7], 2, 20)
    expected = [3, 4, 20, 5, 6, 7]
    assert actual == expected

# def test_midpoint():
#     actual = midpoint(array_length(test),modpoint(test))
#     expected = 2
#     assert actual == expected