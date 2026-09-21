termo=int(input("Digite o primeiro termo da PA : "))
razao=int(input("Digite a razão da PA: "))
print(f"A pa dos numero {termo} com a razão de {razao} é:")
numeros = 0
while numeros != 10:
    pa = termo + (numeros * razao)
    numeros += 1
    print(pa, end=" →")
print(".... ACABOU.")
