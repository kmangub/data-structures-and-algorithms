from challenges.quick_sort.quick_sort import quick_sort

def test_quick_sort():
    arr = [8,4,23,42,16,15]
    actual = quick_sort(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected
