#Algoritmo para encontrar el mayor de tres numeros
num1 = input("Ingrese el valor del numero: ")
num2 = input("Ingrese el valor del numero: ")
num3 = input("Ingrese el valor del numero: ")
print("Los numeros son: ",num1," / ",num2," / ",num3)

if int(num1) < int(num2) > int(num3):
    print ("El numero mayor es:", int(num2))
else:
    if int(num1) > int(num3):
        print("El numero mayor es: ", int(num1))
    else:
        print("El numero mayor es: ", int(num3))
    