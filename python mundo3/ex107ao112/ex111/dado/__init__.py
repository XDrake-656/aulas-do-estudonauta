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
