h=float(input("Quanto voce mede de altura em m? "))
p=float(input("Quanto voce pesa em Kg? "))
imc=p/(h*h)
if imc < 18.5:
    print(f"Seu imc esta a {imc:.2f}. Voce esta abaixo do seu peso ideal.")
elif 18.5 <= imc < 25:
    print(f"Seu imc esta a {imc:.2f}. Voce esta no seu peso ideal.")
elif 25 <= imc < 30:
    print(f"Seu imc esta a {imc:.2f}. Voce esta acima do seu peso ideal.")
elif 30 <=imc < 40:
    print(f"Seu imc esta a {imc:.2f}. Voce esta com obesidade.")
elif imc >= 40:
    print(f"Seu imc esta a {imc:.2f}. Voce esta a um hambúrguer de virar uma baleia.")
