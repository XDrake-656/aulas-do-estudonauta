"""#feito usando o while
num = int(input("qual numero que voce deseje o seu fatorial: "))
fatorial = num
final = 1
while fatorial > 0:
    print(f"{fatorial}", end="")
    print(" X " if fatorial > 1 else " = ", end="")
    final *= fatorial
    fatorial -= 1
print(f"{final}")
print(f"\nA fatorial de {num} é {final}")

"""
#feito usando o for
num = int(input("qual numero que voce deseje o seu fatorial: "))
final = 1
for f in range(num, 0, -1):
    print(f, end="")
    print(" X " if f > 1 else " = ", end="")
    final *= f
print(f"{final}")    
print(f"\nA fatorial de {num} é {final}")    
print("fim")

"""#usando a biblioteca math
from math import factorial
num = int(input("qual numero que voce deseje o seu fatorial: "))
f = factorial(num)
print(f"\nA fatorial de {num} é {f}")
"""
