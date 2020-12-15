def binary_search(arr, num):
    first = 0
    last = len(arr) - 1 
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if arr[mid] == num:
            index = mid
        elif num < arr[mid]:
            last = mid -1
        else:
            first = mid + 1    
    return index



