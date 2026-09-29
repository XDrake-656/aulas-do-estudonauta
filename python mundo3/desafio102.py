def fatorial(num, opc=False):
    """=> FUNÇÃO PARA CALCULAR FATORIAL 
    num : numero que voce quer sua fatorial.
    opc : (opcional) se voce quer mostrar sim ou nao a conta.
    return : o valor da fatorial de um numero n. 
    """
    fat = 1
    if opc == False:
        for c in range(num, 0, -1):
            fat *= c
        return fat
    if opc == True:
        numeros = []
        for c in range(num, 0, -1):
            numeros.append(c)
            fat *= c
        return (" X ".join(map(str, numeros)) + " = " + str(fat))


num = int(input("Digite um numero: "))
opc = " "
while opc not in "SN":
    opc = input("Voce quer que mostre o processo do calculo? [S/N]").strip().upper()[0]
    if opc == "N":
        opc = False
        break
    elif opc == "S":
        opc = True
        break

print(fatorial(num, opc))
