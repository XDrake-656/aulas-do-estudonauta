lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata frita")
print(len(lanche))
print(lanche)
print(lanche[0])
print(lanche[1:])
print(lanche[0:2])
print(lanche[::-1])
print(sorted(lanche))

for comida in lanche:
    print(f"Eu vou comer {comida}")

for possicao in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[possicao]} na posicao {possicao}")
    
for poss, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {poss}")
    
a = (2, 5, 4)
b = (5, 8, 1, 4)
c = a + b
print(c)

pessoa = ("Davi", 25, "M", 2001)
print(pessoa)
del(pessoa)
print(pessoa)
