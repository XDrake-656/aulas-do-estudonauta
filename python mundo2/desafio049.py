n=int(input("Escreva um numero: "))
print(('='*40)+f"\nA tabuada do numero {n} é :")
for t in range(1,11):
    print(f"|{n:3} X {t:2} = {n*t:3}|")
print('{:=^35}'.format(" FIM "))
