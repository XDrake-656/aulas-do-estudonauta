from ex107ao112.ex111 import dado

def moeda(n, f=True):
    if f == True:
        formatado = (f"R${n:.2f}")
        return formatado
    else:
        return n
    
def resumo(n, a=1, d=1, f=True):
    print(("=" * 30) + f"\n{" RESUMO DO VALOR ":^30}\n" + ("=" * 30))
    print(f"Preço analisado:{moeda(n, f):>14}")
    print(f"Dobro do preço: {dado.dobro(n, f):>14}")
    print(f"Metade do preço:{dado.metade(n, f):>14}")
    print(f"{a}% de aumento: {dado.aumentar(n, p = a, f = f):>14}")
    print(f"{d}% de redução: {dado.diminuir(n, p = d, f = f):>14}")
    print("=" * 30)
    
