''' 
<< Bubble Sort Algorithm >>
Sometimes referred to as sinking sort, 
is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted. 
The algorithm, which is a comparison sort, 
is named for the way smaller or larger elements "bubble" to the top of the list.

More info -> https://en.wikipedia.org/wiki/Bubble_sort.
'''
number = input("Enter a number with several digits: ")
digits = list(map(int, str(number)))     # Map digits in number to list
digitsLenght = len(digits)               # Get string lenght
aux = 0                                  # This is to the interchange min and max position
for i in range(digitsLenght-1):          # For each digit in number
  for j in range((digitsLenght-1) - i):  # For each digit in unordered sublist
    if digits[j] > digits[j+1]:          # If digit in lower position is greater than the next digit ...
      aux = digits[j]                    # Temporary copy the grater digit to auxiliar position
      digits[j] = digits[j+1]            # Copy the lower digit to lower position
      digits[j+1] = aux                  # Copy the grater digit to greater index in list

print("Digits ordered from lower to greater:" + str(digits)) # Print ordered list

# See running: https://colab.research.google.com/drive/1bSSMi8pzMevl_xg34rkRU-_POSQXsADk#scrollTo=q4f7Jv2g6YRe&line=8&uniqifier=1
# See interesting discution about list elements interchanges in Python: https://mail.python.org/pipermail/python-es/2006-March/011779.html

