from datetime import datetime

ano = datetime.today().year
print(ano)
pessoa = {}
pessoa["nome"] = input("Digite seu nome: ").strip().title()
pessoa["nascimento"] = int(input("Digite seu ano de nascimento: "))
pessoa["idade"] = ano - pessoa["nascimento"]
pessoa["carteira"] = int(input("Carteira de trabalho: [digite 0 se nao tiver] "))
if pessoa["carteira"] > 0:
    pessoa["contratacao"] = int(input("Qual o ano de contratação: "))
    pessoa["tempo de trabalho"] = ano - pessoa["contratacao"]
    pessoa["salario"] = round(float(input("Salario: R$ ")), 2)
    pessoa["aposentadoria"] = (35 - pessoa["tempo de trabalho"]) + pessoa["idade"]
    print("-="*30)
    for k, v in pessoa.items():
        print(f"{k} = '{v}'")
elif pessoa["carteira"] == 0:
    print("-="*30)
    for k, v in pessoa.items():
            print(f"{k} = '{v}'")
else:
     print("Valor invalido")
