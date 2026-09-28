alunos = {}
alunos["nome"] = input("Digite seu nome: ").strip().title()
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
alunos["media"] = (nota1 + nota2) / 2
print(f"Nome do/a aluno/a é: {alunos["nome"]}")
print(f"A media do/a aluno/a é: {alunos["media"]}")
print("aluno/a Aprovado/a" if alunos["media"] >= 6.00 else "aluno/a Reprovado/a")
