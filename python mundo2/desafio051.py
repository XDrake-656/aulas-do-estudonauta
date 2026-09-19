termo=int(input("Digite o primeiro termo da PA : "))
razao=int(input("Digite a razão da PA: "))
lista = ""
for c in range(10):
    pa = termo + (c * razao)
    print(pa)
    lista = lista, pa  

print("A pa dos numero {} com a razão de {} é ({})".format(termo, razao, lista[1::1]))

