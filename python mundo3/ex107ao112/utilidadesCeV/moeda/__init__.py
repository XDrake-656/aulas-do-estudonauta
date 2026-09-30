def metade(n=0, f=False):
    m = n / 2
    if f == True:
        return moeda(m)
    else:
        return m

def dobro(n=0, f=False):
    d = n * 2
    if f == True:
        return moeda(d)
    else:
        return d

def aumentar(n=0, p=0, f=False):
    por = n * p / 100
    tot = por + n
    if f == True:
        return moeda(tot)
    else:
        return tot
    
def diminuir(n=0, p=0, f=False):
    por = n * p / 100
    tot = n - por
    if f == True:
        return moeda(tot)
    else:
        return tot

def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:.2f}".replace(".",",")
    
    
def resumo(n, a=0, d=0, f=True):
    print(("=" * 30) + f"\n{" RESUMO DO VALOR ":^30}\n" + ("=" * 30))
    print(f"Preço analisado:{moeda(n):>14}")
    print(f"Dobro do preço: {dobro(n, f):>14}")
    print(f"Metade do preço:{metade(n, f):>14}")
    print(f"{a}% de aumento: {aumentar(n, p = a, f = f):>14}")
    print(f"{d}% de redução: {diminuir(n, p = d, f = f):>14}")
    print("=" * 30)
    
