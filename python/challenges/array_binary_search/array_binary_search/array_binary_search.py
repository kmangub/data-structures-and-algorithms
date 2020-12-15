array = [1,2,3,4,5]
number = 5

def search(arr, num):
    for number in arr:
        if number == num:
            return number - 1
    return -1

print(search(array, number))



