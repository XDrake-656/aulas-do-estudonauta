l1=float(input("Escreva um tamanho de uma reta: "))
l2=float(input("escreva um tamanho de uma segunda reta: "))
l3=float(input("escreva um tamanho de uma terceira reta: "))
if l2 + l3 > l1 and l1 + l2 > l3 and l1 + l3 > l2:
    print("O comprimento das retas {}, {} e {} podem formar um triangulo.".format(l1, l2, l3))
else:
    print("O comprimento das retas {}, {} e {} não podem formar um triangulo.".format(l1, l2, l3))
