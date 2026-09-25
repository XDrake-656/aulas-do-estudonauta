lista_num = []
pares = []
impares = []
for c in range(1,8):
    num = int(input(f"Digite o {c}° numero: "))
    lista_num.append(num)

for numero in lista_num:
    if numero % 2 ==0:
       pares.append(numero)
    else:
        impares.append(numero) 
print(f"VocÊ digitou os numeros {lista_num}")
print(f"Os numeros pares digitados foram os {sorted(pares)}")
print(f"Os numeros impares digitados foram os {sorted(impares)}")
