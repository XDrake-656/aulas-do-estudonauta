notas = []
alunos = []
turma = []
while True:
    alunos.append(input("Nome do aluno: ").strip().title())
    notas.append(round(float(input("nota 1: ")),2))
    notas.append(round(float(input("nota 2: ")),2))
    alunos.append(notas[:])
    turma.append(alunos[:]) 
    alunos.clear()
    notas.clear()
    continua = " "
    while continua not in "SN":
        continua = input("Você quer adicinar mais um alunos? [S/N] ").strip().upper()[0]
    if continua == "N":
        break
turma.sort()
print("="*40)
print(f"{'No.':<3} {'NOME':<20} {'MÉDIA':>7}")
print("="*40)
for aluno in range(0, len(turma)):
    print(f"{aluno:<3} {turma[aluno][0]:<20} {(turma[aluno][1][0] + turma[aluno][1][1]) / 2:>7.2f}")
print("="*40)
while True:
    mostrar = int(input("Mostar nota de qual aluno? [digite 999 para parar] "))
    if mostrar in range(0,len(turma)):
        print("="*40)
        print(f"As notas do/da {turma[mostrar][0]} são {turma[mostrar][1]}.")
    elif mostrar == 999:
            break
    elif mostrar not in range(0,len(turma)):
        print("Aluno não encontrado tente novamente\n")
print("FINALIZANDO...")
print("<<<< VOLTE SEMPRE >>>>")
