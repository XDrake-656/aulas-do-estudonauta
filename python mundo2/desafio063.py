"""
print("="*30 + "\nSequencia de Fibonacci\n" + "="*30)
seq = int(input("escreva por quantos elementos da squencia de fibonacci você quer: "))
f0 = 0
f1 = 1
print(f0,"-", f1, end=" - ")
numeros = 3
while numeros != seq:
    f2 = f0 + f1
    print(f2, end=" - ")
    f0 = f1
    f1 = f2 
    numeros += 1
print("fim")
"""
n = int(input('Quantos termos quer? '))
f0 = 0
f1 = 1
f2 = 0
cont = 0
while cont < n:
    print(f"{f2}", end=' - ')
    f0 = f1
    f1 = f2
    f2 = f0 + f1
    cont += 1
print('FIM')
