gols = []
jogador = {}
total_gols = 0
jogador["nome"] = input("Digite seu nome: ").strip().title()
partidas = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
for j in range(1, partidas + 1):
    gol = int(input(f"Quantas gols na partida {j}°? "))
    gols.append(gol)
    total_gols += gol
jogador["gols"] = gols[:]
jogador["total"] = total_gols
print("=-"*30)
print(jogador)
print("=-"*30)
for k, v in jogador.items():
    print(f"{k} = {v}")
print("=-"*30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for c in range(1, partidas + 1):
    print(f"=> Na partida {c}, fez {jogador['gols'][c - 1]} gols.")
print(f"Foi um total de {jogador['total']} gols.")
