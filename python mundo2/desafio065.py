p = False
soma = 0
quatnum = 0
maior = 0
menor = 0
while p != True:
    num = int(input("Digite um numero inteiro: "))
    soma += num
    quatnum += 1
    if quatnum == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    con = str(input("Você quer digitar outro numero(S/N): ")).strip().upper()
    if con == "N":
        media = soma / quatnum
        p = True

print(f"\nA media entre os {quatnum} numeros que você digitou foi de {media:.2f}.")
print(f"O maior numero digitado foi {maior} e o menor foi {menor}.")        
print("fim")
