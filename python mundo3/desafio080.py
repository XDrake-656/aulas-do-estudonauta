lista_numeros = []
for c in range(1, 6):
    num = int(input("Digite um numero: "))
    if c == 1 or num > lista_numeros[-1]:
        lista_numeros.append(num)
    else:
        pos = 0
        while pos < len(lista_numeros):
            if num <= lista_numeros[pos]:
                lista_numeros.insert(pos, num)
                break
            pos += 1
print(lista_numeros)
