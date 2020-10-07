''' 
<< Insertion Sort Algorithm >>
Insertion sort is a simple sorting algorithm that builds the final sorted array 
(or list) one item at a time.  It is much less efficient on large lists than 
more advanced algorithms such as quicksort, heapsort, or merge sort. 

However, insertion sort provides several advantages: 
- Efficient for (quite) small data sets, much like other quadratic sorting algorithms
- Adaptive, stable, in-place, online.

More info: https://en.wikipedia.org/wiki/Insertion_sort
'''
# Getting a set of digits in Python
number = input("Enter a number with several digits: ")
digits = list(map(int, str(number)))        # Map digits in number to list
digitsLength = len(digits)                  # Get string length
aux = 0                                     # To temporary store smaller value

# Insertion Sort Algorithm implementation
for i in range(1, digitsLength):            # Unordered list starts at 2nd position
  j = i                                     # Get first element from unordered list
  while j > 0 and digits[j-1] > digits[j]:  # Compare this with each element to the left.
    aux = digits[j-1]                       # Copy the digit to be replaced to temp variable
    digits[j-1] = digits[j]                 # Copy the lower digit to lower position
    digits[j] = aux                         # Copy the grater digit to greater index in list 
    j-=1                                    # Move to left

print("Digits ordered from lower to greater:" + str(digits)) # Print ordered list

# See running: https://colab.research.google.com/drive/1bSSMi8pzMevl_xg34rkRU-_POSQXsADk?usp=sharing
# See interesting discution about list elements interchanges in Python: https://mail.python.org/pipermail/python-es/2006-March/011779.html
