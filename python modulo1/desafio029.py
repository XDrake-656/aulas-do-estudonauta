v=int(input("Digite a velocidade do carro? "))
print("Você ultrapassou o limite de velocidade!!!! MULTADO em R${:.2f}".format((v-80)*7) if v>80 else "Dentro do limite de velocidade permitido! Tenha um bom dia!")
