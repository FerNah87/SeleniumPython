#Comparar los valores
a = 10
b = 5
c = 16
print("Son iguales " + str(a == b))
print("Son iguales " + str(a == c))
print("A es menor que B " + str(a < b))
print("A es mayor que B " + str(a > b))
print("A es menor o igual que B " + str(a <= b))
print("B es menor o igual que B " + str(b <= a))
print("A es diferente que B " + str(a != b))

#Operacion de comparacion Y (and)
print("1) Si A es menor que B y A es menor que C " + str(a<b and a<c))

##Operacion de comparacion funcion O (or)
print("2) Si A es menor que B y A es menor que C " + str(a<b or a<c))