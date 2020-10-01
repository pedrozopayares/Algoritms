# Bubble Sort ...
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

print("Digits ordered to lower to greater:" + str(digits)) # Print ordered list
