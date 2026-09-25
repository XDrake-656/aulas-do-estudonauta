lista = []
lista_par = []
lista_imp = []
while True:
    num = int(input("Digite um numero: "))
    lista.append(num)
    cont = " "
    while cont not in "SN":
        cont = str(input("Você quer digitar outro numero? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
for numero in range(len(lista)):
    if lista[numero] % 2 == 0:
        lista_par.append(lista[numero])
    else:
        lista_imp.append(lista[numero])

print(f"Os numeros pares são {lista_par}.")
print(f"Os numeros impares são {lista_imp}.")
print(f"Todos os numeros digitados foram os {lista}.")
