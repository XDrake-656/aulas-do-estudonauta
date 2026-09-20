"""#COMO EU FIZ
n=int(input("Digite um numero "))
mult = 0
v = bool
if n == 2:
        v = True
else:
    for c in range(2,n):
        if n % c == 0:
            print(f"multiplo de {c}")
            mult = mult + 1
        if mult == 0:
            v = True
        else:
            v = False
print(f"O numero {n} é primo"if v == True else f"O numero {n} não é primo")

"""
#como o professor fez
num = int(input("digite um numero: "))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print("\033[33m", end="")
        tot = tot + 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
print("\n\033[mO numero {} foi divisivel {} vezes".format(num,tot))
if tot == 2:
    print("E po isso ele é PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
