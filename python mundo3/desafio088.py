from random import randint
from time import sleep
lista = []
print("="*35 + f"\n{"JOGA NA MEGA SENA":^35}\n" + "="*35)
jogos = int(input("Digite quantos jogos você quer sortear? "))
print(f"{f" SORTEANDO {jogos} JOGOS ":=^35}")
for c in range(1,jogos + 1):
    while len(lista) != 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    print(f"jogo {c}: {sorted(lista)}")
    lista.clear()
    sleep(1)
print(f"{f" BOA SORTE! ":=^35}")
