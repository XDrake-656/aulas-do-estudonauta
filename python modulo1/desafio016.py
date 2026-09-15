"""
uma forma de fazer a conversão de um numero real para inteiro é usando a função int()
n=float(input("Digite um numero: "))
print("o numero inteiro digitado é {}".format(int(n)))
"""
import math
n=float(input("Digite um numero: "))
print("O numero digitado {} tem sua parte inteira digitada é {}".format(n, math.floor(n)))
