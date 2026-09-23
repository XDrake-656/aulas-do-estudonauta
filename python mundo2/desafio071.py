# minha solução
print("=" * 35 + f"\n{"BANCO":^35}\n" + "=" * 35)
num = int(input("Que valor você quer sacar? "))
while True:
    if num >= 50:
        n50 = num // 50
        print(f"Total de {n50} cedulas de R$50")
        num -= (n50 * 50)
    if num >= 20:     
        n20 = num // 20
        print(f"Total de {n20} notas de R$20")
        num -=(n20 * 20)
    if num // 10 >= 1:
        n10 = num // 10
        print(f"Total de {n10} notas de R$10")
        num -=(n10 * 10)
    if num // 1 >= 1:
        n1 = num // 1
        print(f"Total de {n1} notas de R$1")
        num -=(n1 *1)
    num = int(input("Que sacar mais algum valor? \nSe NÃO digite [ 0 ] \nSe SIM digite quanto: R$ "))
    if num == 0:
        break
    
print("=" * 35)
print("Obrigado, volte sempre")


# solucao do professor
"""
print("=" * 35 + f"\n{"BANCO":^35}\n" + "=" * 35)
valor = int(input("Que valor você quer sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cedulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10 :
            ced = 1
        totced = 0
        if total == 0:
            break    
print("=" * 35)
print("Obrigado, volte sempre")
"""
#solucao ideal de acordo com a ia usando um metodo de lista
"""
print("=" * 35 + f"\n{'BANCO':^35}\n" + "=" * 35)
num = int(input("Que valor você quer sacar? "))

# O mercado usa uma lista de cédulas. Se amanhã entrar a nota de R$200, é só colocar ela aqui!
cedulas = [200, 100, 50, 20, 10, 2] 

for cedula in cedulas:
    if num >= cedula:
        quantidade = num // cedula  # A sua lógica matemática genial aqui!
        print(f"Total de {quantidade} cédulas de R${cedula}")
        num %= cedula  # O resto da divisão vira o novo valor (substitui o num -= conta)

print("=" * 35)
print("Obrigado, volte sempre")
"""
