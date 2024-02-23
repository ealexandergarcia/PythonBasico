#Algoritmo para convertir grados celsius a fahrenheit
valC = int(input("Ingrese el valode de los grados en Celsius que desea convertir: "))
print("Valor Celsius: ",valC,"°C")
ValF = ((9/5) * valC) + 32
print("Valor Fahrenheit ",round(ValF, 1),"°F")