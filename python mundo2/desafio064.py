c = False
nd = 0
soma = 0
while not c:
    n=int(input("Digite um numero inteiro (para parar o programa digite 999): "))
    if n == 999:
            c = True
    else:
        nd += 1
        soma += n 
print(f"VocÊ digitou {nd} numeros e a soma entre eles é de {soma}")
