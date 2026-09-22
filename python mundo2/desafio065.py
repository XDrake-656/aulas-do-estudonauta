resposta = False
soma = quatnum = maior = menor = 0
while not resposta:
    num = int(input("Digite um numero inteiro: "))
    soma += num
    quatnum += 1
    if quatnum == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    con = str(input("Você quer digitar outro numero(S/N): ")).strip().upper()[0]
    if con == "N":
        media = soma / quatnum
        resposta = True
print(f"\nA media entre os {quatnum} numeros que você digitou foi de {media:.2f}.")
print(f"O maior numero digitado foi {maior} e o menor foi {menor}.")        
print("fim")
