termo=int(input("Digite o primeiro termo da PA : "))
razao=int(input("Digite a razão da PA: "))
print(f"A pa dos numero {termo} com a razão de {razao} é:")
for c in range(10):
    pa = termo + (c * razao)
    print(pa, end=" →")
print(".... ACABOU!")


"""# como o professor fez
termo = int(input("Digite o primeiro termo da PA : "))
razao = int(input("Digite a razão da PA: "))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(pa, end=" →")
print(".... ACABOU!")
"""