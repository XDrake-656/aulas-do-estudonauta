from random import randint
r=randint(0,100)
tentativas = 0
resposta = False
while not resposta: 
    n=int(input("Tente adivinhar o número que estou pensando entre 0 e 100: "))
    tentativas += 1
    if n != r:
            if n > r:
                input("Você errou! Tente um numero MENOR. Aperte enter para tentar novamente.")
            else:
                input("Você errou! Tente um numero MAIOR. Aperte enter para tentar novamente.")
    else:
            resposta = True                 

print(f"Parabéns! Você acertou! eu estava pensando no numero {r}")
if tentativas <= 5:
        print(f"Você foi bem, consiguim em apenas {tentativas} tentativas.")
elif tentativas <= 10:
        print(f"Você conseguim em {tentativas} tentativas.")
else:
       print(f"Você demorou bastante, demorou {tentativas} tentaivas para acertar.")
