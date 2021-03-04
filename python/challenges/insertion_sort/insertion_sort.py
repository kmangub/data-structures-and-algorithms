def insertion_sort(arr):
  index_length = range(1, len(arr))    
  for i in index_length:
    right = arr[i]
       
    while arr[i-1] > right and i>0:
      arr[i], arr[i-1] = arr[i-1], arr[i]
      i -= 1
    
  return arr
            