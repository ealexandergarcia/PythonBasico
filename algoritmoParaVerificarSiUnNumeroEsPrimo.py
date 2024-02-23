#Algoritmo para verificar si un numero es primo
num1 = int(input("Ingrese el numero que desea saber si es primo"))
x = 1
c = 0
while x <= num1:
    if num1 % x == 0:
        c = c +1
    x = x + 1
if c == 2:
    print("El numero ", num1," Si es primo")
else:
    print("El numero ",num1," no es primo")