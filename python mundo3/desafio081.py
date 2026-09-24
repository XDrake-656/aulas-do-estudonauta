lista_num = []
while True:
    num = int(input("Digite um numero: "))
    lista_num.append(num)

    cont = " "
    while cont not in "SN":
        cont = str(input("Você quer digitar outro numero? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
print(f"Você digitou {len(lista_num)}")
lista_num.sort(reverse=True)
print(f"Os numeros digitados em ordem decrescente foram {lista_num}")
print("O numero 5 foi digitado!" if 5 in lista_num else "O numero 5 não foi digitado")
