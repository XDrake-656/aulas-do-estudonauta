sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Qual é seu sexo: (M = masculino, F = feminino) ")).strip().upper()
    if sexo != "M" and sexo != "F":
        resposta=str(input("Você digitou um valor invalido aperte enter para tentar de novo."))

print("Seu sexo é Masculino." if sexo == "M" else("Seu sexo é Feminino."))
