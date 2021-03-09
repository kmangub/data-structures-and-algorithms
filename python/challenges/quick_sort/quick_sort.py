# Solution Derived from Derrick Sherrill's youtube video: https://www.youtube.com/watch?v=kFeXwkgnQ9U&t=45s

def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater = []
    lower = []

    for number in arr:
        if number > pivot:
            greater.append(number)

        else:
            lower.append(number)

    return quick_sort(lower) + [pivot] + quick_sort(greater)

test = [8,4,23,42,16,15]

print(quick_sort(test))