# The Biggest is ...
num = input("Enter a number with several digits: ")
digits = str(num)
digitsLenght = len(digits)
biggest = 0
aux = ''
index = 0
for i in range(digitsLenght-1):
  if digits[i] > digits[i+1]:
    biggest = digits[i]
    aux[index] = biggest
  else:
    biggest = digits[i+1]
print("The biggest digit in number is:" + biggest)
