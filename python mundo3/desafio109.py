from ex107ao112 import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p)}")
print(f"A dobro de {moeda.moeda(p)} é {moeda.dobro(p)}")
print(f"Aumentando 10% de {moeda.moeda(p)}, temos {moeda.aumentar(p, 10)}")
print(f"Reduzindo 13% de {moeda.moeda(p)}, temos {moeda.diminuir(p, 13)}")
