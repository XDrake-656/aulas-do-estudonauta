valores = []
num_men = []
num_mai = []
for posicao in range(1,6):
    valores.append(int(input(f"Digite um valor para a posição {posicao}: ")))
for numero in range(len(valores)): # uma forma simplificada > nummen = [pos for pos, numero in enumerate(valores) if numero == min(valores)]
    if valores[numero] == min(valores):
        num_men.append(numero + 1)
    if valores[numero] == max(valores):
        num_mai.append(numero + 1)
print(valores)
print(f"O maior valor da digitado foi ó ( {max(valores)} ) e ele foi digitado nas posições {'ª...'.join(map(str,num_mai))}ª")
print(f"O menor valor da digitado foi ó ( {min(valores)} ) e ele foi digitado nas posições {'ª...'.join(map(str,num_men))}ª")
