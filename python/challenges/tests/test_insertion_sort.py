from challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort():
    arr = [8,4,23,42,16,15]
    actual = insertion_sort(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected
