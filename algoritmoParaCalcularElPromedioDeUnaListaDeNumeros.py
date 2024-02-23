#Algoritmo para calcular el promedio de una lista de numeros
numeros = [10,20,30,40,50,60,70]

if len(numeros) ==0:
    promedio=0
else:
    sumaTotal = sum(numeros)
    promedio = sumaTotal/len(numeros)

print("El promedio de la lista de numeros es: ", promedio)
