from random import sample
a1=input("Digite o nome do aluno 1: ")
a2=input("Digite o nome do aluno 2: ")
a3=input("Digite o nome do aluno 3: ")
a4=input("Digite o nome do aluno 4: ")
l=sample([a1,a2,a3,a4],k=4)
print("A ordem de apresentação será:{}. ".format(l))
