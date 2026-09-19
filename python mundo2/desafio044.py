valor=float(input("Qual o valor a ser pago pelo produto? "))
print("1= à vista no dinheiro, 2= à vista cartão 3= 2x no cartão ou 4= 3x ou mais no cartao")
forma=int(input("Qual forma de pagamento? digite (1, 2, 3 ou 4): "))
if forma == 1:
    print(f"À vista no dinheiro a sua compra tera um desconto de 10% e ficara em R${valor-((valor*10)/100):.2f}")
elif forma == 2:
    print(f"À vista no cartão a sua compra tera um desconto de 5% e ficara em R${valor-((valor*5)/100):.2f}")
elif forma == 3:
    print(f"No cartão a sua compra não tera almento de preço e ficara em R${valor:.2f} em 2X de R${(valor/2):.2f}.")
elif forma == 4:
    valor_final = valor+((valor*20)/100)
    parcelas = int(input("quantas parcelas de (3x ate 10x)? "))
    possibilidades=[3,4,5,6,7,8,9,10]
    if parcelas in possibilidades:
        parcelas = possibilidades[parcelas]
        valor_dividido = valor_final/parcelas
    else:
        print("voce nao selecionaou uma opcao valida")

    print(f"No cartão a sua compra tera um aumento de 20% e e ficara em R${valor_final:.2f} em {parcelas}X de R${valor_dividido:.2f}.")
else:
    print("Você não digitou opções validas!!!")
