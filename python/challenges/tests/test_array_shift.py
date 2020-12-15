from challenges.array_shift import __version__
from challenges.array_shift.array_shift import insertShiftArray

def test_version():
    assert __version__ == '0.1.0'

def test_insert_number_in_even():
    actual = insertShiftArray([3,4,5,6,7,8], 100)
    expected = [3,4,5,100,6,7,8]
    assert actual == expected

def test_insert_number_in_odd():
    actual = insertShiftArray([3,4,5,6,7], 200)
    expected = [3,4,5,200,6,7]
    assert actual == expected

