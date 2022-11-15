inicio = 1
fin = 100

while(inicio <= fin):
    print("Esto se repite " + str(inicio))
    #si no agrega lo de abajo se crea el bucle infinito
    inicio = inicio +1
    if(inicio == 78):
        break