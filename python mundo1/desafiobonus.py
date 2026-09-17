#Super Desafio:** Criar um Gerenciador de Gastos Pessoais no terminal que avise se o saldo ficar negativo.
s=float(input("Digite quanto você ganhou esse mes: "))
g=float(input("Digite quanto você gastou esse mes: "))
cores={'limpa':'\033[m',
       'verde':'\033[1;32m',
       'vermelho':'\033[1;31m',
       'preto':'\033[7;37m'}
if s > g:
    print("O saldo deste mes foi {}POSSITIVO!!!{} com um lucro de {}R${:.2f}{}.".format(cores['verde'], cores['limpa'], cores['verde'], s-g, cores['limpa']))
elif s == g:
    print("O saldo do mes foi {}NEUTRO{}, nao teve nem ganho nem prejuizo.".format(cores['preto'], cores['limpa']))
else:
    print("O saldo do mes foi {}NEGATIVO!!!{} com um prejuizo de {}R${:.2f}{}.".format(cores['vermelho'], cores['limpa'], cores['vermelho'], s-g, cores['limpa']))
