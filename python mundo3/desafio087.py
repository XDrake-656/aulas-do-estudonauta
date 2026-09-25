matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for linha in range(0,3):
   for coluna in range(0, 3):
      matriz[linha][coluna] = int(input(f"digite um valor para [{linha}], [{coluna}]: "))
for linha in range(0, 3):
    for coluna in range(0, 3):
      print(f"[{matriz[linha][coluna]:^5}]", end="")
      if (matriz[linha][coluna]) % 2 ==0:
         pares += matriz[linha][coluna]
    print()
print(f"A soma dos valores pares é {pares}.")
print(f"A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.")
print(f"O maior valor da segunda lina é {max(matriz[1])}.")
