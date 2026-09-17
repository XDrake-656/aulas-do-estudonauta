#testando o uso do if e else
""" 
nome=str(input("Digite seu nome: ")).title().strip()
if "Davi" in nome:
    print("Seu nome é lindo!")
else:
    print("Que nome é normal!")
print("Bom dia {}!".format(nome))
"""

#testando condicao simplificada
n1=float(input("Digite sua primeira nota:"))
n2=float(input("Digite sua segunda nota:"))
m=(n1+n2)/2
print("Sua média foi {:.1f}".format(m))
print("Parabens!!!!" if m>=6 else "Estude mais!!!!")
