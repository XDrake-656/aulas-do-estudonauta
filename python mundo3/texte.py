texte = ["((a+b)*c)"]
abre = ["("]
fecha = [")"]
casa = 0
verdadeiro = False

for c in range(len(texte)):
    print(texte[c])
    if c in abre:
        casa += 1
    if c in fecha:
        casa -= 1
if casa == 0:
    verdadeiro = True

if verdadeiro == True:
    print("Expressão valida!")
else:
    print("Expressão não valida!")    