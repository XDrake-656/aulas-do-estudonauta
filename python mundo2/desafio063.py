'''f0 = 0
f1 = int(input("escreva um numero inteiro: "))
seq = int(input("escreva por quantos elementos da squuencia de fibonacci você quer: "))
f2 = f1 + f0
c = 0
while c != seq:
    if c == 0:
        print(f0)
    elif c == 1:
        print(f1)
    elif c == 2:
        print(f2)
    elif c == 3:
        print(f1 + f2)
    else:
        f0 = f0 + f1
        print("f0",f0)
        f1 = f1 + f0
        print("f1",f1)
        f2 = f2 + f1
        print("f2",f2)
        fn = f2 + f1
        print("fn",fn)

    c += 1
    
print("fim")
'''

numero = 0
elemento = 100
while numero != elemento:
    print
