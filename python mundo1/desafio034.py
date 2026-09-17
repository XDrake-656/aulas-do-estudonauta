s=float(input("Qual é seu salario? "))
if s <=1250.00:
    print("Parabens voce vai receber um aumento de salario de 15% ou seja agora voce recebe R${:.2f}.".format((s+(s*15)/100)))
else:
    print("Parabens voce vai receber um aumento de salario de 10% ou seja agora voce recebe R${:.2f}.".format(s+((s*10)/100)))
