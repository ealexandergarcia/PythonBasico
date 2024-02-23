#Algoritmo para generar la serie Fibonacci
num1= int(input("Ingrese el numero que desea usar para la serie: "))
a=0
b=1

for i in range(num1):
    c=b+a
    a=b
    b=c
print("El valor de la serie es: ", a)
