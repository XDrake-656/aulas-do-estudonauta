maior = 0
menor = 0

for p in range(1, 6):
    peso=float(input("Qual seu peso, em Kg? "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso lido foi {maior:.2f}")
print(f"O menor peso lido foi {menor:.2f}")
