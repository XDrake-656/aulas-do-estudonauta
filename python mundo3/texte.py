galera = [["João", 50.00], ["Ana", 45.00], ["Joaquim", 70.00], ["wesley", 70.00], ["Maria", 60.00]]
maior = max(galera, key=lambda peso: peso[1])
print(maior[1])

turmaA = [['Ana', [1.0, 2.0]], ['Davi', [3.0, 4.0]], ['Kaio', [5.0, 6.0]]]
turmaB = [['Alan', [7.0, 8.0]], ['David', [9.0, 10.0]], ['Caio', [11.0, 12.0]]]
turmas = [
    [
        ['Ana', [1.0, 2.0]], ['Davi', [3.0, 4.0]], ['Kaio', [5.0, 6.0]]
        ],
        [
            [['Alan', [7.0, 8.0]], ['David', [9.0, 10.0]], ['Caio', [11.0, 12.0]]]
         ]
]
#turmas.sort()
print(turmas)
print(turmas[0][0][1][0])
print(turmas[0][0][1][1])
print(turmas[0][1][1][0])
print(turmas[0][2][1][1])


grupo = [{'nome': 'Davi', 'sexo': 'M', 'idade': 25}, {'nome': 'Maria', 'sexo': 'F', 'idade': 18}]
print(grupo[1]["idade"])

print("\033[41mEste é um aviso com a linha inteira vermelha!\033[K\033[m")
print("\033[42mLinha inteira verde para sucesso!\033[K\033[m")