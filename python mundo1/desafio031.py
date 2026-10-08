d=int(input("Escreva a distancia da sua viagem em Km:"))
if d<=200:
    print(f"Para essa viagem de {d}Km, o preço da passagem sera de R${d*0.50:.2f}.")
else:
    print(f"para viagens acima de 200Km damos um desconto no valor das passagens. Como essa viagem é de {d}Km, voce recebera um desconto de 10% então a sua passagem sera R${d*0.45:.2f}")
    