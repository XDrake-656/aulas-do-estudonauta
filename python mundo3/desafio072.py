tupla = ("Zero", "Um", "Dois", "Treis", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
        numero = -1
        while numero not in range(0,21):
                numero = int(input("digite um numero entre 0 e 20: "))        
        print(f"Você digitou o numero {tupla[numero]}")
        cont = str(input(f"Você quer digitar outro numero?[S/N] ")).strip().upper()[0]
        if cont == "N":
                break
print("fim")
