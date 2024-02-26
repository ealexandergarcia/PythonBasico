from os import system #import of the standard function os.system()

#Tupla de informacion general del user
name = input("Ingrese el nombre: ")
age = input("Ingrese la edad: ")
height = input("Ingrese la altura: ")
basicInfo = (name,age,height)

#Tupla sobre las direcciones del user
x = input("Tiene mas de una direccion? (si/no)")
if x.lower() == "si":
    address = input("Ingrese el su direccion: ")
    address1 = input("Ingrese el su direccion: ")
else:
    address = input("Ingrese el su direccion: ")
    address1= "no aplica"
addresses = (address,address1)

#Tupla sobre la educacion del user
askBasicEdu = input("Cuenta con algun curso tecnico/tecnologo? (si/no): ")
basicEdu = "no aplica"
professionalEdu = "no aplica"
if askBasicEdu.lower() == "si":
    print("Ingrese el nombre del curso")
    basicEdu = input("")

askProfessionalEdu = input("Cuenta con algun titulo universitario? (si/no): ")
if askProfessionalEdu.lower() == "si":
    print("Ingrese el nombre del titulo")
    professionalEdu = input("")  
education = (basicEdu,professionalEdu)

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
workExperience = (experience,experience1)

system("clear")

print(f"""
---------------------------------------------------
INFORMACION BASICA    
Nombre: {basicInfo[0]}
Edad: {basicInfo[1]}
Altura: {basicInfo[2]}
---------------------------------------------------
DIRECCIONES 
Direccion principal: {addresses[0]}
Direccion secundaria: {addresses[1]}
---------------------------------------------------
INFORMACION ACADEMICA
Curso tecnico/tecnologo: {education[0]}
Titulo universitario: {education[1]}
---------------------------------------------------
EXPERIENCIA LABORAL
Primer experiencia laboral: {workExperience[0]}
Segunda experiencia laboral: {workExperience[1]} """)