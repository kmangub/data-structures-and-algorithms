# def array_length(arr):
#     return len(test)

# def insert_number(arr, index, number):
#   arr.insert(index, number)
#   return arr

def insertShiftArray(arr, num):
  array_length = len(arr)

  if array_length % 2:
    middle_array = round(array_length // 2) + 1
  else:
    middle_array = array_length // 2

  arr.insert(middle_array, num)
  return arr


# print(insert_number(test, index, insert_value))
# input('> ')
# Determine first if it's odd or even
# Insert the number to the left 
