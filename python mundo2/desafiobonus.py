from random import choice
from time import sleep
palavras_facil = ("BOLA", "CASA", "GATO", "DADO", "LAGO", "MESA", "SAPO", "RATO", "BOLO", "CAJU", "COPO", "LIMA", "POTE", "LUA", "SOL")
palavras_medio = ("BANANA", "CANETA", "ESCADA", "JIRAFA", "MACACO", "PANELA", "TIJOLO", "PIPOCA", "CAVALO", "RAPOSA", "PASSARINHO", "LIMONADA", "TOMATE", "JANELA", "ALFACE", "ROUPA", "SAFARI")
palavras_dificil = ("ALFABETO", "CHOCOLATE", "DINOSSAURO", "COMPUTADOR", "ELEFANTE", "GIRAFA", "HELICOPTERO", "PARALELEPIPEDO", "QUADRADO", "TRAVESSEIRO", "ZOOLODICO", "VAMPIRO", "QUILOMETRO", "AMENDOIM", "ARQUITETO")
respostas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print(f"{" FORCA ":=^40}" + """\nVamos jogar forca, as regras são: 
[1] = Você tera 6 oportunidades para chutar uma letra e acertar a palavra
[2] = Você so tera uma chance para acertar a palavra se errar perdeu
[3] = Você não deve usar acentos nas palavras
[4] = Você pode escolher a dificuldade do jogo digitando (1 facil / 2 medio / 3 dificil)""")

nivel = int(input("\nesolha a dificuldade(1/2/3): "))

if nivel == 1:
    palavra = choice(palavras_facil)
elif nivel == 2:
    palavra = choice(palavras_medio)
elif nivel == 3:
    palavra = choice(palavras_dificil)
letras = list(palavra)
print(f"ok voce escolheu o nivel {nivel} vamos comessar!")
sleep(2)
print("estou pensando em palavra......")
sleep(2)
print(f"OK a palavra que estou pensando tem {len(palavra)} letras")

tentativas = 1
letras_chutadas = ""
while tentativas != 7:
    if tentativas == 6:
            print("\n\nEssa É sua ultima tentativa agora tente acertar a palavra") 
    
    chute = str(input("\n\nChute uma letra ou tente descobrir a palavra: ")).strip().upper()
    
    if len(chute) > 1:
        tentativas = 7
        if chute == palavra:
            print(f"Você acertou!!! a palavra era mesmo {palavra}")
            print(f"Você chutou essas letras {letras_chutadas}.")
            print(f"\033[1;32m{"YOU WIN":=^40}\033[m")
            
        else:
            print(f"Você errou, a palavra que sorteada era {palavra} e nao {chute}.")
            print(f"Você chutou essas letras {letras_chutadas}.")
            print(f"\033[1;31m{"GAME OVER":=^40}\033[m")

    if len(chute) == 1:
        if chute in respostas:
            tentativas += 1
            letras_chutadas = str(letras_chutadas) + str(chute)
            for letra in letras:
                if chute == letra or letra in letras_chutadas:
                    print("\033[1;32m", end=" ")
                else:
                    print("\033[8;41m", end=" ")
                print(letra, end=" ")
                print("\033[m", end=" ")

        else: 
            erro=str(input("voce digitou uma resposta invalida, aperte 'ENTER' para tentar de novo: "))
