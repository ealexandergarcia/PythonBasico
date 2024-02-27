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
        "Aceitunas": 3500,
        "Promociones": 
            ([{"Baguette": 1000, "cantidad": 3},
              {"Baguette": 1000, "cantidad": 3}])
    },
    "Bolleria": {
        "Croissant": 1500,
        "Dona": 1250,
        "Palmera": 1750,
        "Napolitana de chocolate": 2000,
        "Ensaimada": 2500,
        "Muffin": 1750,
        "Tartaleta de frutas": 2250,
        "Churro": 1500,
        "Pain au chocolat": 2250,
        "Berlina": 2000
    },
    "Galletas": {
        "Galletas de mantequilla": 1000,
        "Alfajores": 1250,
        "Orejas de elefante": 1500,
        "Pastas de té": 1000,
        "Barquillos": 1500,
        "Rosquillas": 1250,
        "Galletas de avena": 1750,
        "Biscotti": 2000,
        "Galletas de jengibre": 1500,
        "Madeleines": 2250
    }
}


print("Categorías disponibles:")
for i,categoria in enumerate(panaderia_dict):
    print(f"{i}. {categoria}")

categoria_elegida = input("Elige una categoría (Pan/Bollería/Galletas y pastas): ").capitalize()
if categoria_elegida in panaderia_dict:
    print(f"Productos en la categoría {categoria_elegida}:")
    for producto, precio in panaderia_dict[categoria_elegida].items():
        print(f"  - {producto}: ${precio}")
else:
    print("Categoría no válida. Por favor, elige una categoría existente.")


selection = input(f"""Que producto desea: """)
if selection in panaderia_dict[categoria_elegida]:
    amount= int(input(f"""Cuantos {selection} desea: """))
    finalPrice = amount * panaderia_dict[categoria_elegida][selection]
    print(f"""El valor de su compra es de: ${finalPrice}""")
    dinero = int(input("Ingrese la cantidad de dinero disponible: "))
    vueltos = finalPrice - dinero
    if finalPrice <= dinero:
        print(f"Tome su {selection} disfrutela rey, sus vueltos son {-vueltos}")
    else:
        print(f"Usuario el producto que desea comprar {selection} con un valor de ${panaderia_dict[categoria_elegida][selection]}, le falta un total de ${vueltos}")
else:
    print("Categoría no válida. Por favor, elige una categoría existente.")