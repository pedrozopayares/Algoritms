# The Biggest is ...
num = input("Enter a number with several digits: ")
digits = str(num)
digitsLenght = len(digits)
biggest = 0
for i in range(digitsLenght):
     for j in range (digitsLenght-1):
          if digits[j] > digits[j+1]:
                biggest = digits[j]
          else:
                biggest = digits[j+1]
print("The biggest digit in number is:" + biggest)
