#Algoritmo para generar una tabla de multiplicar
num1= int(input("Ingrese la tabla de multiplicar que desea saber: "))

print("Tabla del ",num1)
for i in range (11):
    resultado = num1 * i
    print(num1,"*",i," = ",resultado)
