#input nos permite guardar datos en la variable

print("cual es tu nombre: ")
nombre = input()
print("cual es tu apellido: ")
apellido = input()
print("cual es tu edad: ")
edad = input()

print("Valor de A: ")
a = input()
a = int(a)
print("Valor de B: ")
b = input()
b = int(b)
sumar = a + b

print("tu nombre es {} {} {} ".format(nombre, apellido, edad))
print("la suma de {} + {} = {} ".format(a, b, sumar))