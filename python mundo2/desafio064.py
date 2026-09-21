c = " "
final = ""
nd = 0
soma = 0
while c != final:
    n=int(input("Digite um numero inteiro (para parar o programa digite 999): "))
    if n == 999:
            c = ""
    else:
        nd += 1
        soma += n
    
print("fim")
print(f"VocÊ digitou {nd} numeros e a soma entre eles é de {soma}")
