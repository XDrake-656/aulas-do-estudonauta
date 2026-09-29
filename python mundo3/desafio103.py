def ficha(nome = "", gols = 0):
    if nome == "":
        nome = "<desconhecido>"
    return f"O jogador {nome} fez {gols} gol(s) no campeonato"

nome = input("Nome do jogador: ").strip().title()
gols = int(input("Numero de gols: ") or "0")
print(ficha(nome, gols))
