"""
uma forma de resolver
co=float(input("Digite o comprimento do cateto oposto: "))
ca=float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da Hipotenusa é {:.2f}".format(((co**2)+(ca**2))**(1/2)))
"""
import math
co=float(input("Digite o comprimento do cateto oposto: "))
ca=float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da Hipotenusa é {:.2f}".format(math.hypot(ca,co)))
