def metade(n, f=True):
    m = n / 2
    if f == True:
        formatado = (f"R${m:.2f}")
        return formatado
    else:
        return m

def dobro(n, f=True):
    d = n * 2
    if f == True:
        formatado = (f"R${d:.2f}")
        return formatado
    else:
        return d

def aumentar(n, p = 1, f=True):
    por = n * p / 100
    tot = por + n
    if f == True:
        formatado = (f"R${tot:.2f}")
        return formatado
    else:
        return tot
    
def diminuir(n, p = 1, f=True):
    por = n * p / 100
    tot = n - por
    if f == True:
        formatado = (f"R${tot:.2f}")
        return formatado
    else:
        return tot

def moeda(n, f=True):
    if f == True:
        formatado = (f"R${n:.2f}")
        return formatado
    else:
        return n
    
def resumo(n, a=1, d=1, f=True):
    print(("=" * 30) + f"\n{" RESUMO DO VALOR ":^30}\n" + ("=" * 30))
    print(f"Preço analisado:{moeda(n, f):>14}")
    print(f"Dobro do preço: {dobro(n, f):>14}")
    print(f"Metade do preço:{metade(n, f):>14}")
    print(f"{a}% de aumento: {aumentar(n, p = a, f = f):>14}")
    print(f"{d}% de redução: {diminuir(n, p = d, f = f):>14}")
    print("=" * 30)
    
