'''
teste = []
galera = []
teste.append("Davi")
teste.append(25)
galera.append(teste[:])
teste[0] = ("Maria")
teste[1] = (22)
galera.append(teste[:])
print(galera)
'''
'''
galera = [["João", 19], ["Ana", 33], ["Joaquim", 50], ["Maria", 15]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")
'''
galera = list()
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input("Nome: ")).strip().title())
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade")
        menor += 1
print(f"Temos {maior} pessoas maiores de idade e {menor} menores de idade.")
