print(('-+-'*30)+ "\nParabens você decidiu financiar uma casa, preencha as informações abaixo: ")
casa=float(input("Qual o valor da casa que você deseja financiar? "))
salario=float(input("quanto você ganha mensamente? "))
anos=int(input("por quantos anos você pretende dividir as parcelas? "))
prestacao = casa / (anos*12)
if prestacao >= (salario*30)/100:
    print("A prestacao desta casa em {} anos, ficara em R${:.2f}. Infelismente seu salaria de R${:.2f} nao cobre esse valor. \033[1;31memprestimo negado.\033[m".format(anos, prestacao, salario))
else:
    print("A prestacao desta casa em {} anos, ficara em R${:.2f}. Parabens com um salario de R${:.2f} atende aos requisitos. \033[1;32memprestimo aprovado.\033[m".format(anos, prestacao, salario))
print('-+-'*30)
