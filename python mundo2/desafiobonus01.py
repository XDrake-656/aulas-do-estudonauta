#Refasendo desafio bonus do mundo 1
#Super Desafio:** Criar um Gerenciador de Gastos Pessoais no terminal que avise se o saldo ficar negativo.
from time import sleep
totalGanho = 0
totalGastos = 0
cores={'limpa':'\033[m',
       'verde':'\033[1;32m',
       'vermelho':'\033[1;31m',
       'preto':'\033[7;37m'}
while True:
    pergunta = int(input("""Voce quer adicionar 
[1] = adicionar GANHOS
[2] = adicionar GASTOS
[3] = parar 
digite: """))
    if pergunta == 1:
        while True:
            s = float(input("Digite o valor ganho (digite '0' para parar): "))
            if s == 0:
                    break
            else:
                totalGanho += s    
    elif pergunta == 2:
        while True:
            g = float(input("Digite seus gastos (digite '0' para parar): "))
            if g == 0:
                break
            else:
                totalGastos += g
    elif pergunta == 3:
        break        
    else:
        print("Você digitou um valor invalido tente denovo")
        sleep(2)    
            
print(f"Voce adiquiriu {cores['verde']}R${totalGanho:.2f}{cores['limpa']} esse mes.")
print(f"os gastos totais desse mes foram de {cores['vermelho']}R${totalGastos:.2f}{cores['limpa']}.")
if totalGanho > totalGastos:
    print(f"O saldo deste mes foi {cores['verde']}POSSITIVO!!!{cores['limpa']} com um lucro de {cores['verde']}R${totalGanho-totalGastos:.2f}{cores['limpa']}.")
elif totalGanho == totalGastos:
    print(f"O saldo do mes foi {cores['preto']}NEUTRO{cores['limpa']}, nao teve nem ganho nem prejuizo.")
else:
    print(f"O saldo do mes foi {cores['vermelho']}NEGATIVO!!!{cores['limpa']} com um prejuizo de {cores['vermelho']}R${abs(totalGanho-totalGastos):.2f}{cores['limpa']}.")
