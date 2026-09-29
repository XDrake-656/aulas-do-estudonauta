from time import sleep
def contagem(inicio, fim, passo):
    print("=-"*20)
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} ate {fim} de {abs(passo)} em {abs(passo)}")
    if inicio > fim:
        fim -= 1
        passo = -abs(passo)
    elif inicio < fim:
        fim += 1
        passo = abs(passo)
    for c in range(inicio, fim, passo):
        print(f"{c}", end=" ", flush = True)
        sleep(0.5)
    print("\nFIM DA CONTAGEM")

contagem(1,10,1)
contagem(10,0,-2)
print("Agora é a sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("passo em passo: "))
contagem(i, f, p)
