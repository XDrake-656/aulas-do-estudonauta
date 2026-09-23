numlist = pares = ()
for c in range(1,5):
    num = int(input("Digite um numero: "))
    numlist += (num,)
    if num % 2 == 0:
        pares += (num,)
print(numlist)
print(f"O numero 9 apareceu {numlist.count("9")} vezes.")
print("O numero 3 não foi digitado em nenhuma posição" if numlist.count(3) == 0 else f"O numero 3 apareceu pela primeira vez na {(numlist.index(3)) + 1}ª posição.")
print(f"Os numeros pares digitados são {pares}")
