from ex107ao112 import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de {p:.2f} é {moeda.metade(p):.2f}")
print(f"A dobro de {p:.2f} é {moeda.dobro(p):.2f}")
print(f"Aumentando 10% de {p:.2f}, temos {moeda.aumentar(p, 10):.2f}")
print(f"Reduzindo 13% de {p:.2f}, temos {moeda.diminuir(p, 13):.2f}")
