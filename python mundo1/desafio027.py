n=str(input("Digite seu nome completo:")).title().strip()
print("Considerando o nome {} ele tem como primeiro nome '{}' e como ultimo nome '{}'".format(n, n.split()[0], n.split()[-1]))
