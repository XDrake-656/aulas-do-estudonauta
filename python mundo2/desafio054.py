from datetime import date
ano = date.today().year
grupo = 0
grupo_menor = 0
grupo_maior = 0
for c in range(0,7):
    nascimento=int(input("Em que ano voce nasceu ? "))
    idade = (ano - nascimento)
    grupo = grupo + 1
    print (idade)
    if  idade < 21:
        grupo_menor = grupo_menor + 1
        print("voce é menor de idade")
    else:
        grupo_maior = grupo_maior + 1
        print("voce é maior de idade")
print(f"nesse grupo de {grupo} pessoas tem {grupo_menor} menores de idade e {grupo_maior} maiores de idade.")
print("final")
