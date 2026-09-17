nome=str(input("Digite seu nome: "))
cor={'limpa':'\033[m', 
     'vermelho':'\033[1;31m',
     'azul':'\033[4;34m',
     'preto':'\033[7;37m'}
print("Ola, muito prazer em te conhecer, {}{}{}!!!!!".format(cor['azul'], nome, cor['limpa']))
