numero = input("Ingrese un número: ")
numeroString = str(numero)
numeroLenght = len(numeroString)
mayor = 0
for i in range(numeroLenght):
     espacioDesordenado = i
     for j in range (espacioDesordenado - 1):
          if numeroString[j] > numeroString[j+1]:
                mayor = numeroSstring[j]
          else:
                mayor = numeroString[j+1]
print(mayor)
