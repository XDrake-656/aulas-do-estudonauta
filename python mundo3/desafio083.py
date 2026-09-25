operadores =['+','-','*','/']
casa = 0
verdadeiro = False
operacao = False
exp = str(input("digite a expressão: ")).strip()
expressao = list(exp)
while "(" in expressao:
    expressao.remove("(")
    casa += 1
while ")" in expressao:
    expressao.remove(")")
    casa -= 1
if casa == 0:
    verdadeiro = True
else:
    verdadeiro = False

for f in range(1,len(expressao),2):
    if expressao[f] not in operadores:
        operacao = False
    else:
        operacao = True

if verdadeiro == operacao == True:
    print("Expressão valida!")
else:
    print("Expressão não valida!")
