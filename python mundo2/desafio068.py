from random import randint
from time import sleep
computador = randint(1, 100)
jogos_ganhos = 0
print(("=-="*5) + "VAMOS JOGAR PAR OU IMPAR" + ("=-="*5))
while True:
    jogador_esc = " "
    while jogador_esc not in 'PI':
        jogador_esc = str(input("Par ou Impar?[P/I] ")).strip().upper()[0]
    jogador_num = int(input("Digite um valor: "))
    soma = computador + jogador_num
    print("Par ....")
    sleep(1)
    print("ou ....")
    sleep(1)
    print("Impar ....")
    sleep(1)
    if soma % 2 == 0:
        print(f"Você jogou {jogador_num} e o computador jogou {computador}. Total de {soma} DEU PAR")
        if jogador_esc == "P":
            print("VOCÊ VENCEU!\nVamos jogar novamente ...")
            jogos_ganhos += 1
        else:
            print("VOCÊ PERDEU!")
            break
    else:
        print(f"Você jogou {jogador_num} e o computador jogou {computador}. Total de {soma} DEU IMPAR")
        if jogador_esc == "I":
            print("VOCÊ VENCEU!\nVamos jogar novamente ...")
            jogos_ganhos += 1
        else:
            print("VOCÊ PERDEU!")
            break   
print(f"GAME OVER! Você venceu {jogos_ganhos} vezes.")
