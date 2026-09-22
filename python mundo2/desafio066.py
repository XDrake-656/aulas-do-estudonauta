quanum = soma = 0
while True:
    num = int(input("Digite um numero inteiro(para parar digite '999'): "))
    if num == 999:
        break
    quanum += 1
    soma += num
print(f"Você digitou {quanum} numeros e o resultado da soma entre eles é {soma}.")
