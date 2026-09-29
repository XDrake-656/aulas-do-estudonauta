from datetime import datetime
atual = datetime.today().year

def voto(nascimento):
    if (atual - nascimento) >= 65 or ((atual - nascimento) >= 16 and (atual - nascimento) <= 18):
        return "Opcional"
    elif (atual - nascimento) >= 19:
        return "Obrigatorio"
    else:
        return "Negado"

nascimento = int(input("Qual ano voce nasceu? "))
print(f"como você tem {atual - nascimento} anos, o voto é {voto(nascimento)}")
