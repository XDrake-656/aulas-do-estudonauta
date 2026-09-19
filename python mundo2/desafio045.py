from random import randrange
from time import sleep
import emoji

jogadas = {'1': '📃', '2': '✂', '3': '🪨'}

print('-+-'*20 + '\n'"vamos jogar jakenpô")
print(emoji.emojize("1 para 📃 / 2 para ✂ / 3 para 🪨"))
j = str(input("digite sua jogada:")).strip()

if j in jogadas:
    j = jogadas[j]
    o = jogadas[str(randrange(1,4))]
else:
    print('-+-'*20)
    print("voce usou um valor errado!")
    print('-+-'*20)

print("vamos la \nJA.....")
sleep(1)
print("KEN .....")
sleep(1)
print("PÔ.....")
sleep(1)

if (j == "📃" and o == "🪨") or (j == "✂" and o == "📃") or (j == "🪨" and o == "✂"):
        print(f"{j} ganha de {o} Parabéns!!!, você ganhou!!!")
elif (o == "📃" and j == "🪨") or (o == "✂" and j == "📃") or (o == "🪨" and j == "✂"):
    print(f"{j} perde para {o} eu ganhei!!!")
else:
    print(f"Os dois jogaram {j} ! Deu empate.")
print('-+-'*20)
