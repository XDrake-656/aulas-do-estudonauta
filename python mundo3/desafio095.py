gols = []
jogador = {}
jogadores = []
while True: 
    print("="*40)
    total_gols = 0
    jogador["nome"] = input("Digite seu nome: ").strip().title()
    jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
    for j in range(1, jogador["partidas"] + 1):
        gol = int(input(f"Quantas gols na partida {j}°? "))
        gols.append(gol)
        total_gols += gol
    jogador["gols"] = gols[:]
    jogador["total"] = total_gols
    jogadores.append(jogador.copy())
    gols.clear()
    continua = " "
    while continua not in "SN":
            continua = input("VocÊ quer adicinar mais um usuario? [S/N] ").strip().upper()[0]
    if continua == "N":
        break
print("=-"*40)
print(f"{"COD NOME":<20}{"GOLS":<15}{"TOTAL":5}")
print("="*40)
for j, jog in enumerate(jogadores, start = 1):
    print(f"{j:<3} {jog['nome']:<17}{', '.join(map(str, jog['gols'])):<15}{jog['total']:>5}")
while True:
    continua = -1
    while continua != 999:
        print("="*40)
        continua = int(input("Mostrar dados de qual jogador?[999 para parar]  "))
        if continua in range(1, len(jogadores) + 1):
            print(f"{" LEVANTAMENTO DO JOGADOR ":=^40}"f"\n{jogadores[continua - 1]["nome"]:^40}")
            for c in range(1, (jogadores[continua - 1]["partidas"]) + 1):
                print(f"=> Na partida {c}, fez {jogadores[continua - 1]['gols'][c - 1]} gols.")
            print(f"Foi um total de {jogadores[continua - 1]['total']} gols.")
        elif continua > len(jogadores) and continua != 999:
                print("Valor não valido! tente outro")
                continue
    if continua == 999:
            break
print("="*40)
print("FIM")
