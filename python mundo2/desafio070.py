total = alto = barato = 0 
nome_barato = ""
print("-" * 35 + f"\n{"LOJA":^35}\n" + "-" * 35)
while True:
    nome = str(input("Qual o nome do produto: ")).strip()
    preco = float(input("Preço: R$"))
    if preco > 1000:
        alto += 1
    if total == 0 or preco < barato:
        nome_barato = nome
        barato = preco
    total += preco    
    continuar  = ""
    while continuar != "S" and continuar != "N":
        continuar  = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"{"FIM DO PROGRAMA":-^35}")    
print(f"O total da compra foi de R${total:.2f}")
print(f"Temos {alto} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi '{nome_barato}' que custa R${barato:.2f}.")
