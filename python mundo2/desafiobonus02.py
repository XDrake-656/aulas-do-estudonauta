from random import choice
from time import sleep
palavras_facil = ("BOLA", "CASA", "GATO", "DADO", "LAGO", "MESA", "SAPO", "RATO", "BOLO", "CAJU", "COPO", "LIMA", "POTE", "LUA", "SOL")
palavras_medio = ("BANANA", "CANETA", "ESCADA", "JIRAFA", "MACACO", "PANELA", "TIJOLO", "PIPOCA", "CAVALO", "RAPOSA", "PASSARINHO", "LIMONADA", "TOMATE", "JANELA", "ALFACE", "ROUPA", "SAFARI")
palavras_dificil = ("ALFABETO", "CHOCOLATE", "DINOSSAURO", "COMPUTADOR", "ELEFANTE", "GIRAFA", "HELICOPTERO", "PARALELEPIPEDO", "QUADRADO", "TRAVESSEIRO", "ZOOLODICO", "VAMPIRO", "QUILOMETRO", "AMENDOIM", "ARQUITETO")
respostas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print(f"{" FORCA ":=^40}" + """\nVamos jogar forca, as regras são: 
[1] = Você tera algumas oportunidades para chutar uma letra e acertar a palavra
[2] = Você so tera uma chance para acertar a palavra se errar perdeu
[3] = Você não deve usar acentos nas palavras ou caracteres especiais
[4] = Você pode escolher a dificuldade do jogo digitando (1 facil / 2 medio / 3 dificil)
[5] = Quanto mais dificil MENOS chutes você vai ter.""")

nivel = int(input("\nesolha a dificuldade(1/2/3): "))

if nivel == 1:
    palavra = choice(palavras_facil)
    max_tentativas = 8
elif nivel == 2:
    palavra = choice(palavras_medio)
    max_tentativas = 7
elif nivel == 3:
    palavra = choice(palavras_dificil)
    max_tentativas = 6
letras = list(palavra)
print(f"ok voce escolheu o nivel {nivel} vamos comessar!")
sleep(2)
print("estou pensando em uma palavra......")
sleep(2)
print(f"OK a palavra que estou pensando tem {len(palavra)} letras \ne você tem {max_tentativas - 1} tentativas para acertar a palavra.")

tentativas = 1
letras_chutadas = ""
ganhou = False

while tentativas != max_tentativas:
    if tentativas == max_tentativas - 1:
            print("\n\nEssa É sua ultima tentativa agora tente acertar a palavra") 
    
    chute = str(input("\n\nChute uma letra ou tente descobrir a palavra: ")).strip().upper()
    
    if len(chute) > 1:
        if chute == palavra:
            ganhou = True
            break

    if len(chute) == 1:
        if chute not in respostas:
            print("\033[1;31mEntrada inválida! Digite apenas letras de A a Z sem CARACTERES ou ACENTUAÇÃO.\033[m")
            continue

        
        tentativas += 1
        letras_chutadas += str(chute)
        todas_letras_descobertas = True
        for letra in letras:
            if chute == letra or letra in letras_chutadas:
                print("\033[1;32m", end=" ")
            else:
                print("\033[8;41m", end=" ")
                todas_letras_descobertas = False
            print(letra, end=" ")
            print("\033[m", end=" ")
        if todas_letras_descobertas:
            ganhou = True
            break    

if ganhou == True:
    print(f"Você acertou!!! a palavra era mesmo {palavra}")
    print(f"Você chutou essas letras {letras_chutadas}.")
    print(f"\033[1;32m{"YOU WIN":=^40}\033[m")
            
else:
    print(f"Você errou, a palavra que sorteada era {palavra} e nao {chute}.")
    print(f"Você chutou essas letras {letras_chutadas}.")
    print(f"\033[1;31m{"GAME OVER":=^40}\033[m")
