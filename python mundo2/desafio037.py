'''
# codigo limpo e simplis
n=int(input("Escreva um numero inteiro qualquer: "))
b=int(input("Escreva para qual sera a base de conversão 1= 'binario', 2= 'octal', 3= 'hexadecimal': "))
if b == 1:
    print("O numero {} em binario se escreve {}.".format(n, bin(n)))
elif b == 2:
    print("O numero {} em octal se escreve {}.".format(n, oct(n)))
elif b == 3:
    print("O numero {} em hexadecimal se escreve {}.".format(n, hex(n)))
else:
    print("Você não escreveu uma base de conversao aceitavel!!!")
'''
'''
# codigo fica bem limitado e nao consegui pensar em uma forma para fazer com hexadecimal
n=int(input("Escreva um numero inteiro entre 0 e 128: "))
b=int(input("Escreva para qual sera a base de conversão 1= 'binario'ou 2= 'octal': "))
binario = str((n//128) % 2)+str((n//64) % 2)+str((n//32) % 2)+str((n//16) % 2)+str((n//8) % 2)+str((n//4) % 2)+str((n//2) % 2)+str(n % 2)
octal = str((n//64) % 8)+str((n//8) % 8)+str(n % 8)
if b == 1:
    print("O numero {} em binario se escreve {}.".format(n, binario))
elif b == 2:
    print("O numero {} em octal se escreve {}.".format(n, octal))
else:
    print("Você não escreveu uma base de conversao aceitavel!!!")
'''

#feito com ajuda da ia (codigo sem os comandos proprios de conversao de base)
n=int(input("Escreva um numero inteiro qualquer: "))
b=int(input("Escreva para qual sera a base de conversão 1= 'binario', 2= 'octal', 3= 'hexadecimal': "))

def converter_para_base(numero, base):
    if numero == 0:
        return "0"
    caracteres = "0123456789ABCDEF"
    resultado = ""
    while numero > 0:
        resto = numero % base
        resultado = caracteres[resto] + resultado
        numero = numero // base
        
    return resultado

binario = converter_para_base(n, 2)
octal = converter_para_base(n, 8)
hexadecimal = converter_para_base(n, 16)

if b == 1:
    print("O numero {} em binario se escreve {}.".format(n, binario))
elif b == 2:
    print("O numero {} em octal se escreve {}.".format(n, octal))
elif b == 3:
    print("O numero {} em hexadecimal se escreve {}.".format(n, hexadecimal))
else:
    print("Você não escreveu uma base de conversao aceitavel!!!")
