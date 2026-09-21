from time import sleep
num1 = 0
num2 = 0
programa = 4
while programa != 5:
    if programa == 4:
            print("digite novos numeros:")
            num1 = int(input("Primeiro numero: "))
            num2 = int(input("segundo numero: "))

    programa=int(input('{:=^40}'.format(" menu ") + f"""
numeros selecionados {num1} e {num2}
[1] = somar
[2] = multiplicar
[3] = para saber qual dos 2 é maior
[4] = trocar numeros
[5] = sair do programa
qual das opções acima você deseja realizar: """))
    if programa == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
        programa=input("aperte [5] para parar ou enter para voltar para o menu.") or 0
        programa=int(programa)
    elif programa == 2:
        print(f"{num1} X {num2} = {num1*num2}")
        programa=input("aperte [5] para parar ou enter para voltar para o menu.") or 0
        programa=int(programa)
    elif programa == 3:
        if num1 > num2:
            print(f"O numero {num1} é maior que {num2}.")
        elif num2 > num1:
            print(f"O numero {num2} é maior que {num1}.")
        else:
            print(f"Os numeros {num1} e {num2} são iguais.")
        programa=input("aperte [5] para parar ou enter para voltar para o menu.") or 0
        programa=int(programa)
    
    if programa == 5:
        print("fechando programa....")
        sleep(2)

    elif programa > 5:
        print("voce digitou um valor não valido")
        programa=input("aperte [5] para parar ou enter para voltar para o menu.") or 0
        programa=int(programa)

print("programa finalizado!")
