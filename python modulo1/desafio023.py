""" -primeira tentativa 
n=str(input("Digite um numero de 0 a 9999:"))
n=n.zfill(4)
print("o numero digitado {} \ntem as sua unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}".format(n,n[3],n[2],n[1],n[0]))
"""
n =int(input("Digite um numero de 0 a 9999: "))
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10
print("O numero digitado {} \ntem a unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}".format(n,u,d,c,m))
