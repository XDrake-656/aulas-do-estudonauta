pessoa = maiores = homens = mulheres_novas = 0
while True:
    pessoa += 1
    print("-"*35 + "\n  CADASTRE UMA PESSOA \n" + "-"*35)
    idade = int(input("Qual a sua idade? "))
    sexo = ""
    while sexo != "M" and sexo !="F":
         sexo = str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0]
    print("-"*35)
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_novas += 1
    interromper = ""
    while interromper != "N" and interromper != "S":
         interromper = str(input("quem cadastrar mais uma pessoa? [S/N] ")).strip().upper()[0]
    if interromper == "N":
            break
print(f"{"FIM DO PROGRAMA":=^35}")
print(f"A quantidade de pessoas cadastradas com mais de 18 anos foi de {maiores}.")
print(f"A quantidade de homens cadastrados foi de {homens}.")
print(f"A quantidade de mulheres com menos de 20 anos cadastradas foi de {mulheres_novas}.")
