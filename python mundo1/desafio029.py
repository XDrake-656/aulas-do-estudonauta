v=int(input("Digite a velocidade do carro? "))
print(f"Você ultrapassou o limite de velocidade!!!! MULTADO em R${(v-80)*7:.2f}" if v>80 else "Dentro do limite de velocidade permitido! Tenha um bom dia!")
