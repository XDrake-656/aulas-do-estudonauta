d=int(input("Escreva a distancia da sua viagem em Km:"))
if d<=200:
    print("Para essa viagem de {}Km, o preço da passagem sera de R${:.2f}.".format(d, (d*0.50)))
else:
    print("para viagens acima de 200Km damos um desconto no valor das passagens. Como essa viagem é de {}Km, voce recebera um desconto de 10% então a sua passagem sera R${:.2f}".format(d, d*0.45))
    