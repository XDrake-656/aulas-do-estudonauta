# falhei no exercicio porem tentei de novo no dia seguinte e consegui 
lista = []
for c in range(0,6):
    num = int(input("Digite um numero: "))
    if c == 0 or num >= max(lista):
        lista.append(num)
        
    elif num <= min(lista):
        lista.insert(0,num)
        
    else:
        posicao = 0
        while posicao in range(len(lista)):
            if num <= lista[posicao]:
                lista.insert(posicao,num)
                break
            posicao += 1    
print(lista)

#solução do professor
'''
lista_numeros = []
for c in range(1, 6):
    num = int(input("Digite um numero: "))
    if c == 1 or num > lista_numeros[-1]:
        lista_numeros.append(num)
    else:
        pos = 0
        while pos < len(lista_numeros):
            if num <= lista_numeros[pos]:
                lista_numeros.insert(pos, num)
                break
            pos += 1
print(lista_numeros)
'''
