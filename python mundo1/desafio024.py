n=str(input("Digite o nome de sua cidade:"))
S="SANTO"
s=n.strip().upper().split()[0]
print(f"sua cidade começa com Santo:{s == S}")
