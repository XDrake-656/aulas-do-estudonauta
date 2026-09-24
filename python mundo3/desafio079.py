lista_numeros = []
while True:
    num = int(input("Digite um numero: "))
    if num not in lista_numeros:
        lista_numeros.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor ja presente na lisata....")
    
    contn = " "
    while contn not in "SN":
        contn = str(input("Você quer digitar outro numero? [S/N] ")).strip().upper()[0]
    if contn == "N":
        break
print(lista_numeros)
print(sorted(lista_numeros))
