from os import system #import of the standard function os.system()
system("clear")
panaderia_dict = {
    "Pan": {
        "Baguette": 2500,
        "Integral": 3000,
        "Centeno": 2750,
        "Molde": 2250,
        "Maiz": 2500,
        "Avena": 3250,
        "Nueces": 3500,
        "Pasas": 3000,
        "Queso": 3750,
        "Aceitunas": 3500
    },
    "Bolleria": {
        "Croissant": 1500,
        "Dona": 1250,
        "Palmera": 1750,
        "Napolitana": 2000,
        "Ensaimada": 2500,
        "Muffin": 1750,
        "Tartaleta": 2250,
        "Churro": 1500,
        "Pain": 2250,
        "Berlina": 2000
    },
    "Galletas": {
        "Galletas de mantequilla": 1000,
        "Alfajores": 1250,
        "Orejas de elefante": 1500,
        "Pastas de te": 1000,
        "Barquillos": 1500,
        "Rosquillas": 1250,
        "Galletas de avena": 1750,
        "Biscotti": 2000,
        "Galletas de jengibre": 1500,
        "Madeleines": 2250
    },
    "Promociones": {
        "Baguette": 1000,
        "Centeno": 1000,
        "Alfajores": 800,
        "Rosquillas": 800,
        "Dona": 850,
        "Croissant": 1000
    }
}
print("Categorias disponibles:")
for categoria in panaderia_dict:
    if categoria != "Promociones":
        print(f" - {categoria}")

categoria_elegida = input("Elige una categoria (Pan/Bolleria/Galletas y pastas): ").capitalize()
if categoria_elegida in panaderia_dict:
    print(f"Productos en la categoria {categoria_elegida}:")
    catSel = panaderia_dict[categoria_elegida]
    for producto, precio in catSel.items():
        print(f"  - {producto}: ${precio}")

    selection = input("¿Que producto desea?: ").capitalize()
    if selection in catSel:
        if selection in panaderia_dict["Promociones"]:
            promo_price = panaderia_dict["Promociones"][selection]
            print(f"¡Hay una promocion! Si compra mas de 3, el precio individual con descuento seria: ${promo_price}")
            amount = int(input(f"Cantidad de {selection} deseada: "))
            if amount >= 3:
                finalPrice = amount * promo_price
                print(f"El valor de su compra con descuento es de: ${finalPrice}")
            else:
                finalPrice = amount * catSel[selection]
                print(f"El valor de su compra es de: ${finalPrice}")
        else:
            amount = int(input(f"Cantidad de {selection} deseada: "))
            finalPrice = amount * catSel[selection]
            print(f"El valor de su compra es de: ${finalPrice}")

        dinero = int(input("Ingrese la cantidad de dinero disponible: "))
        vueltos = finalPrice - dinero
        if finalPrice <= dinero:
            print(f"Aqui tiene su producto ({selection}). ¡Disfrutelo! Sus vueltos son: ${-vueltos}")
        else:
            print(f"Usuario, el producto que desea comprar ({selection}) con un valor de ${catSel[selection]} le falta un total de ${vueltos}")
    else:
        print("Producto no encontrado en la categoria seleccionada.")
else:
    print("Categoria no valida. Por favor, elija entre Pan, Bolleria o Galletas y pastas.")
