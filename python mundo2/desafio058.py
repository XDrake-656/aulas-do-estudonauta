from random import randint
r=randint(0,10)
tentativas = 1
n = 0
while n != r: 
    n=int(input("Tente adivinhar o número que estou pensando entre 0 e 10:"))
    if n != r:
           input("Você errou! aperte enter para tentar novamente.")
           tentativas += 1

print(f"Parabéns! Você acertou! eu estava pensando no numero {r}")
if tentativas <= 3:
        print(f"Você foi bem, consiguim em apenas {tentativas} tentativas.")
elif tentativas <= 6:
        print(f"Você conseguim em {tentativas} tentativas.")
else:
       print(f"Você demorou bastante, demorou {tentativas} tentaivas para acertar.")
