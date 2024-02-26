"""
tupla info
tupla dirreccion
tupla educacion
tupla de exp laboral"""
#Tupla de informacion general del user
nombre = input("Ingrese el nombre: ")
edad = input("Ingrese la edad: ")
altura = input("Ingrese la altura: ")
info = (nombre,edad,altura)

#Tupla sobre las direcciones del user
x = input("Tiene mas de una direccion? (si/no)")
if x.lower() == "si":
    direccion = input("Ingrese el su direccion: ")
    direccion1 = input("Ingrese el su direccion: ")
else:
    direccion = input("Ingrese el su direccion: ")
    direccion1= "Ninguna"

direcciones = (direccion,direccion1)


#Tupla sobre la educacion del user
askBasicEdu = input("Cuenta con algun curso tecnico/tecnologo? (si/no): ")
basicEdu = "No tiene curso tecnico/tecnologo"
askProfessionalEdu = input("Cuenta con algun titulo universitario? (si/no): ")
professionalEdu = "No tiene titulo universitario"
if askBasicEdu.lower() == "si":
    print("Ingrese el nombre del curso")
    basicEdu = input("")
elif askProfessionalEdu.lower() == "si":
    print("Ingrese el nombre del titulo")
    professionalEdu = input("")

education = (basicEdu,professionalEdu)
print(education)

#Tupla sobre la exp laboral
ask = input("Tiene experiencia laboral? (si/no)")
if ask.lower() == "si":
    ask = input("Tiene mas de una experiencia laboral? (si/no)")
    if ask.lower() == "si":
        experience = input("Ingrese su primer experiencia laboral: ")
        experience1 = input("Ingrese su segunda experiencia laboral: ")
    else:
        experience = input("Ingrese su primer experiencia laboral: ")
        experience1= "no aplica"
else:
    experience= "no aplica"
    experience1= "no aplica"
print("exp laboral:")
workExperience = (experience,experience1)
print(f"""Primer experiencia laboral: {workExperience[0]}
Segunda experiencia laboral: {workExperience[1]} """)