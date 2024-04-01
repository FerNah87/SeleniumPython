#Funciones simples sin argumentos
def saludo():
    print("Saludos (Funciones simples)")
    print("Saludos Python")
    a = 20
    b = 30
    c = a + b
    print("Esto es una suma {} + {} = {}".format(a, b, c))
print("Esto es una funcion")
saludo()

#Funciones con Parametros
def saludar():
    print("Hola como estas (Funciones con Parametros)")
def salir():
    print("Hasta luego")
def suma(a , b):
    resultado = a + b
    print("La suma es: " + str(resultado))

saludar()
suma(7, 9)
salir()

#Funciones con Parametros 2
def datos(nomb, apell):
    print("El nombre es {} {} ".format(nomb, apell))

datos("Fer", "Zalasar")
datos("Gry", "Catu")
datos("Tucu", "Cervera")

#Funcion args: la funcion puede recibir N valor
def sumar(*args):
    resultado = 0
    for n in args:
        resultado = resultado + n
    print("El resultado es: " + str(resultado))

sumar(5,9)