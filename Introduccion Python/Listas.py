lenguajes = ["Php" , "Java" , "Python" , "JavaScript"]

print("Lenguaje Seleccionado " + lenguajes[2])

lenguajes[2] = "Django"

print("Lenguaje " + lenguajes[2])

#Agregar un lenguaje
lenguajes.append("Groovy")
print(lenguajes)
#Remover un lenguaje
lenguajes.remove("Java")
print(lenguajes)