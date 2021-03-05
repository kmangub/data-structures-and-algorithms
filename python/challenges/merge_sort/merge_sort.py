
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = int(len(arr) / 2)
    
    left = merge_sort(arr[:midpoint]) 
    right = merge_sort(arr[midpoint:])
   

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    new_array = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_array.append(left[i])
            i += 1
        else:
            new_array.append(right[j])
            j += 1

    new_array.extend(left[i:])
    new_array.extend(right[j:])

    return new_array

sample = [5,4,3,2,1]

print(merge_sort(sample))