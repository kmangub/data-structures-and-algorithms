# Insertion Sort

```
1  def insertion_sort(arr):
2
3    # How many times to iterate
4    index_length = range(1, len(arr)) 
5  
6    # For Loop to compare values
7    for i in index_length:
8      right = arr[i]
9
10      # code will continue to run until 
11      the current number is in the right place
12      while arr[i-1] > right and i>0:
13        arr[i], arr[i-1] = arr[i-1], arr[i]
14        i -= 1
15      
16    return arr
```
Today, I'm going to show you how to implement insertion sort. 

Suppose we have an list called `arr` shown below:

```
arr = [8,4,23,42,16,15]
```

and the we want the expected output to be:

```
[4,8,15,16,23,42]
```

The idea here is that we are comparing two numbers and if the number on the **left** is greater than the number on the **right**, we will need to switch the number placements. 

We need to break down the list into two components: **sorted** and **unsorted**. Here's a visual of how to break down the list:

```
        
[  8,   4,   23,   42,   16,  15  ]
|____| |__________________________|
sorted           unsorted
```

The first one is easy since 8 is the only number in the first portion of the array. No further action is required. 

As we move forward with the algorithm, we will also need to keep track of how many times we are iterating through the array. 

Since 8 is already "sorted", there's no need to perform the sorting operation, meaning we will iterate the length of our array subtracted by 1, or 5 times. This will be represented by 

```
arr = [8,4,23,42,16,15]
length(arr) = 6

index_length = len(arr) - 1

index_length = 5
```
Going back to our array, 


```
        v
[  8,   4,   23,   42,   16,  15  ]
|____| |__________________________|
sorted           unsorted
```

we will move the first number of the unsorted portion of the array (4) to sorted and compare it to the left of it (8).

```
        v
[  8,   4,   23,   42,   16,  15  ]
|________| |______________________|
  sorted           unsorted
```

We see that 4 is not in the right spot, so we need to  switch it with 8. 

In code, this can be achieved with a while loop:

```
1    for i in index_length:
2      right = arr[i]
3
4      while arr[i-1] > right and i>0:
5        arr[i], arr[i-1] = arr[i-1], arr[i]
6        i -= 1
```

Breaking our code down, the current index is 1. The right variable is index 1 of our list, or 4, and we are comparing it to index 0 of our list, or 8. Since 8 is greater than 4, we proceed to line 5 of the code right above, which assigns the numbers to the correct index.

So the new assignment is as follows:

```
arr = [8,4,23,42,16,15]

------------

i = 1

arr[i-1] = arr[(1) - 1] = arr[0] = 4

arr[i] = arr[(1)] = 8
```

And now our array so far should look like this:

```
        
[  4,   8,   23,   42,   16,  15  ]
|________| |______________________|
  sorted           unsorted
```

Now that 8 is greater than 4, we can break out of the loop and go to the next index. 

```
index = 2

             v
[  4,   8,   23,   42,   16,  15  ]
|________| |______________________|
  sorted           unsorted
```

Same as last time, we will move the first number of the unsorted portion of the array (23) to the end of the  sorted section and compare it to the left (8).

```
index = 2

             v
[  4,   8,   23,   42,   16,  15  ]
|______________| |________________|
  sorted              unsorted
```

As we can see, 8 is not greater than 23, so no action is required and we move to the next index.


```
index = 3

                   v
[  4,   8,   23,   42,   16,  15  ]
|_____________________|  |________|
        sorted            unsorted
```

Likewise for 42, we move on to the next index.

> NOTE: Watch closely to the index. Right now, we are at index 4 and we will need to subtract 1 from our index because of our code. Once all the numbers are in the correct order, we will come back to index 4.

```
index = 4

                         v
[  4,   8,   23,   42,   16,  15  ]
|__________________________| |____|
          sorted            unsorted
```

We jump into our while loop and reassign 16 and 42 since 42 is greater than 16. We subtract 1 from our index and we continue through our loop.  

```
index = 3

      while arr[i-1] > right and i>0:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1

                   v
[  4,   8,   23,   16,   42,  15  ]
|__________________________| |____|
          sorted            unsorted
```

We are reassigning 23 and 16 since 23 is greater than 16. 

```
index = 3

      while arr[i-1] > right and i>0:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1

             v
[  4,   8,   16,   23,   42,  15  ]
|__________________________| |____|
          sorted            unsorted
```

This looks right, it's time to move to the next index.

```
index = 5

                              v
[  4,   8,   16,   23,   42,  15  ]
|_________________________________|
               sorted            
```

We jump to our while loop.

```
index = 5

      while arr[i-1] > right and i>0:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1

                              v
[  4,   8,   16,   23,   42,  15  ]
|_________________________________|
               sorted   
```

Since42 is greater than 15, we reassign the numbers and subtract 1 to our index

```
index = 4

      while arr[i-1] > right and i>0:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1
                         v
[  4,   8,   16,   23,   15,  42  ]
|_________________________________|
               sorted            
```

We repeat the operation until 15 is in the correct index,

```
             v
[  4,   8,   15,   16,   23,  42  ]
|_________________________________|
               sorted            
```

Now that we have exhausted the number of iterations, we return the sorted array.

Big thanks to **Derrick Sherrill** for explaining it this way. The algorithm he used makes a lot of sense to me. You can watch his explanation of his code [here](https://www.youtube.com/watch?v=byHi41L9vTM&list=LL&index=1).

