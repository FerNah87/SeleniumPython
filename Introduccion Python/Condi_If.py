#Condicional If
a = 20
b = 10
if (a > b):
    print("El mayor es: " + str(a))
else:
    print("El mayor es: " + str(b))

#igual
nom = "Fernando"
if (nom == "Fernando"):
    print("Tu nombre es: " + nom)

#menor o igual
if(a<=b):
    print("{} es menor o igual que {} ".format(a, b))
else:
    print("Entonces {} no es menor o igual que {} ".format(a, b))

#diferencia
if(a!=b):
    print("{} es diferente que {} ".format(a, b))
else:
    print("Entonces son iguales")

#Condicional If - 2 (elseif condicionamos algo mas) combianciones
a = 40
b = 20
c = 10
if(a>b and a>c):
    print("El mayor es " + str(a))
elif(b>a and b>c):
    print("El mayor es: " + str(b))
elif(c>a and c>b):
    print("El mayor es: " + str(c))

#Condiciona o ||
if(a<b or a>c):
    print("{} < {} o {} > {} ".format(a, b, a, c))