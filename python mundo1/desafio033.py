n1=int(input("Escreva um numero: "))
n2=int(input("escreva um segundo numero: "))
n3=int(input("escreva um terceiro numero: "))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O maior numero é {}.".format(maior))
menor = n1
if n2 < n1 and n3 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("O menor numero é {}.".format(menor))
