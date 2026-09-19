l1=float(input("Qual o tamanho da linha 1? "))
l2=float(input("Qual o tamanho da linha 2? "))
l3=float(input("Qual o tamanho da linha 3? "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f"O comprimento das retas {l1}, {l2} e {l3} podem formar um triangulo")
    if l1 == l2 == l3:
        print("\033[4;32m'todos os lados formarâo um triangulo equilatero.'\033[m")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("\033[4;34m'todos os lados formarâo um triangulo isósceles.'\033[m")
    elif l1 != l2 != l3:
        print("\033[4;35m'todos os lados formarâo um triangulo escaleno.'\033[m")
else:
    print(f"O comprimento das retas {l1}, {l2} e {l3} \033[4;31m'não podem formar um triangulo'\033[m")
