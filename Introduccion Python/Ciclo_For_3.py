#Por medio del ciclo for condicionar un resultado
#Continue es para que no imprima el numero 3 6 9
for num in range(1, 11):
    if (num == 3 or num == 6 or num == 9):
        continue
    print(num)