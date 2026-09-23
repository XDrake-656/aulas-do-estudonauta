from random import randint
lista = ()
maior = menor = 0
for c in range(1, 6):
    n = randint(1,10)
    lista += (n,)
print(lista)
print(f"O maior numero foi {max(lista)}")
print(f"O menor numero foi {min(lista)}")
