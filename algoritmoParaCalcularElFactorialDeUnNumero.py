#Algoritmo para calcular el factorial de un numero
num1 = input("Ingrese el valor del numero que quiere saber su factorial: ")
num1 = int(num1)
result = 1
for i in range( 1, num1 + 1):
    result *= i


print(num1,"! =",result)