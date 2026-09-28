pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(f"O {pessoas["nome"]} tem {pessoas["idade"]} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f"{k} = {v}")

del pessoas["sexo"]    
for k, v in pessoas.items():
    print(f"{k} = {v}")

pessoas["nome"] = "Davi"
for k, v in pessoas.items():
    print(f"{k} = {v}")

pessoas["peso"] = 74.00
for k, v in pessoas.items():
    print(f"{k} = {v}")

Brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(estado1)
print(estado2)
print(Brasil[0]["uf"])
print(Brasil[1]["sigla"])

brasil = list()
estado = dict()
for c in range(0, 3):
    estado["uf"] = input("Unidade federativa: ")
    estado["sigla"] = input("Sigla do Estado: ")
    brasil.append(estado.copy())
# com range
for u in range(len(brasil)):
    print(f"O estado de {brasil[u]["uf"]} tem como sigla {brasil[u]["sigla"]}")
# com enumarate
for c, estado in enumerate(brasil):
    print(f"O estado de {estado["uf"]} tem como sigla {estado["sigla"]}")
# com 2 for
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
