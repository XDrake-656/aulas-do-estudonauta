num = [2, 5, 7, 1, 5, 5, 5]
num[1] = 9 # mudando valor da variavel
num.append(7) # adicinando variavel
num.sort(reverse=False) # ordenando a lista
num.insert(1, 9) #adicionando variavel na posicao que eu quero
while 5 in num: # removendo todos as variaveis iguais
    num.remove(5)
print(num)
print(len(num)) # contando quantidade de variaveis

#usuario colocando valores na lista
"""valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: "))) # usuario adiciando variaveis na lista

for c, v in enumerate(valores):
    print((f"Na posição {c} eu encontrei o valor {v}!"))
print("FIM")
"""
a = [2, 4, 6, 8,]
b = a # cria uma copia porem ligada a lista a ou seja se uma das duas forem modificadas as duas sao mudadas
c = a[:] # agora sim criou uma copia da lista a 
b[1] = 8
print(f"lista a: {a}.")
print(f"lista b: {b}.")
print(f"lista b: {c}.")
