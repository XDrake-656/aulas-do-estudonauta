n=str(input("Digite o nome de sua cidade:"))
S="SANTO"
s=n.strip().upper().split()[0]
print("sua cidade começa com Santo:{}".format(s == S))