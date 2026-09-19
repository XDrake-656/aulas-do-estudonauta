n=int(input("Escreva um numero: "))
print(('='*40)+f"\nA tabuada do numero {n} é :")
for t in range(1,11):
    print("|{:3} X {:2} = {:3}|".format(n, t , n*t))

print('{:=^35}'.format(" FIM "))
