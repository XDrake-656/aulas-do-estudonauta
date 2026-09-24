lista_numeros = []
for c in range(1, 6):
    num = int(input("Digite um numero: "))
    if c == 1:
        lista_numeros.append(num)
    else:
        for numeros in range(len(lista_numeros) - 1, -1, -1):
            if num == lista_numeros[numeros]:
                lista_numeros.insert(numeros, num)
                break
            if num > lista_numeros[numeros]:
                lista_numeros.insert(numeros + 1, num)
                break  
            if num < lista_numeros[numeros]:
                lista_numeros.insert(numeros - 1,num)
                break
print(lista_numeros)
