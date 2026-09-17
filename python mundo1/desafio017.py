"""
uma forma de resolver
co=float(input("Digite o comprimento do cateto oposto: "))
ca=float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da Hipotenusa é {:.2f}".format(((co**2)+(ca**2))**(1/2)))
"""
from math import hypot
co=float(input("Digite o comprimento do cateto oposto: "))
ca=float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da Hipotenusa é {:.2f}".format(hypot(ca,co)))
