from random import randint


def sorteia():
    numeros = []
    for n in range(1,6):
        sorteado = randint(1,10)
        numeros.append(sorteado)
    return numeros
lista = sorteia()
def somapar(lst):
    p = 0
    for n in lst:
        if n % 2 == 0:
            p += n
    return p
print(f"OS valores sorteados foram {lista}")
print(f"Somando os valores pares de {lista} temos {somapar(lista)}")
