#Algoritmo para calcular el area de un circulo
radio = int(input("Ingrese el valor del radio: "))

if radio <= 0:
    print("No se puede usar un radio menor a 0")
else:
    area = (3.14159) * (radio**2)
    print("El area del circulo es: ", area)
