n = 1
par = imp = 0
while n != 0:
    n = int(input("Digite um numero par ou impar(quando quiser que o programa pare digite 0): "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            imp += 1
            
print(f"voce digitou {par} numeros pares e {imp} numeros imapres")
