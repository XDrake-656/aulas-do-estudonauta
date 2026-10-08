l1=float(input("Escreva um tamanho de uma reta: "))
l2=float(input("escreva um tamanho de uma segunda reta: "))
l3=float(input("escreva um tamanho de uma terceira reta: "))
if l2 + l3 > l1 and l1 + l2 > l3 and l1 + l3 > l2:
    print(f"O comprimento das retas {l1}, {l2} e {l3} '\033[4;34m'podem formar um triangulo.'\033[m'")
else:
    print(f"O comprimento das retas {l1}, {l2} e {l3} '\033[4;31m'não podem formar um triangulo.'\033[m'")
