valor = 0
for c in range(0,6):
    n=int(input("Escreva um numero inteiro: "))
    print(f"numero digitado foi {n}.")
    if n % 2 == 0:
        valor += n
print(f"a soma dos numeros impares digitados é {valor}.")
