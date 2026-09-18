n=str(input("Qual o seu nome? ")).strip()
if n.upper() == "DAVI":
    print("Que nome bonito!")
elif n.upper() in ("PAULO MARIA ANA JOAO"):
    print("Seu nome me é familiar.")
else:
    print("Que nome comum!")
print("Tenha um bom dia, {}!".format(n))
