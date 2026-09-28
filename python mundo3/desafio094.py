grupo = []
pessoa = {}
while True:
    pessoa["nome"] = input("Digite seu nome: ").strip().title()
    pessoa["sexo"] = " "
    while pessoa["sexo"] != "M" and pessoa["sexo"] != "F":
        pessoa["sexo"] = input("Digite seu sexo:[M/F] ").strip().upper()[0]
    pessoa["idade"] = int(input("Digite sua idade: "))

    grupo.append(pessoa.copy())

    continua = " "
    while continua not in "SN":
            continua = input("VocÊ quer adicinar mais um usuario? [S/N] ").strip().upper()[0]
    if continua == "N":
        break
media = 0
for k in range(len(grupo)):
     print(grupo[k]["idade"])
     media += grupo[k]["idade"]
media_total = media / len(grupo)
mulheres = []
for f in range(len(grupo)):
     
print(grupo)
print(f"O grupo tem {len(grupo)} pessoas.")
print(f"A media de idade é de {media_total:.2f}")
print(f"As mulheres cadastradas foram: {}")
