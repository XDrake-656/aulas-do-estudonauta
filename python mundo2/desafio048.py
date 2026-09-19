soma=0
for c in range(0,501):
    if (c % 2) == 1:
        if (c % 3) == 0:
            print(c)
            soma = soma + c
print(f"a soma de todos os numeros impares que sao multiplos de 3 e = a {soma}")
