n=str(input("Digite seu nome completo:")).title().strip()
print(f"Considerando o nome {n} ele tem como primeiro nome '{n.split()[0]}' e como ultimo nome '{n.split()[-1]}'")
