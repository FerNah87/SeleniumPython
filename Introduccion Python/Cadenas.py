texto = "Hola Bienvenidos a Python"

print(texto)
print(texto[3])
print(texto[5:15])
print(texto[5:])
print(texto[-6:])

#Funciones con cadenas
nombre = "Fernando"

print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())

cadena = "php, java, selenimum, javascript"
print(cadena)
print(cadena.split(','))

#Imprimir valores de cadena con .format
name = "Ferchu"
lastn = "Snake"
age = 35
print("Mi nombre es {} mi apellido es {} y mi edad es {} ".format(name, lastn, age))