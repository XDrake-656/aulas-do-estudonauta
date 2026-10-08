s=float(input("Qual é seu salario? "))
if s <=1250.00:
    print(f"Parabens voce vai receber um aumento de salario de 15% ou seja agora voce recebe R${s+(s*15)/100:.2f}.")
else:
    print(f"Parabens voce vai receber um aumento de salario de 10% ou seja agora voce recebe R${s+((s*10)/100):.2f}.")
