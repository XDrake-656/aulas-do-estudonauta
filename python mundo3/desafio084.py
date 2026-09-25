usuario = []
grupo = []
pesadas = []
leves = []
while True:
    usuario.append(input("Digite seu nome: ")).strip().title()
    usuario.append(round(float(input("Digite seu peso em Kg: ")),2))
    grupo.append(usuario[:]) 
    
    usuario.clear()
    continua = " "
    while continua not in "SN":
        continua = input("VocÊ quer adicinar mais um usuario? [S/N] ").strip().upper()[0]
    if continua == "N":
        break
maior_peso = max(grupo, key=lambda peso: peso[1])[1]
menor_peso = min(grupo, key=lambda peso: peso[1])[1]
for pessoa in grupo:
    if pessoa[1] == maior_peso:
        pesadas.append(pessoa[0])
    if pessoa[1] == menor_peso:
            leves.append(pessoa[0])
        
print(f"\n{len(grupo)} pessoas foram cadastradas.")
print(f"O maior peso foi de {maior_peso[1]:.2f}Kg. Essas pessoas tem esse peso {", ".join(pesadas)}")
print(f"O menor peso foi de {menor_peso[1]:.2f}Kg. Essas pessoas tem esse peso {", ".join(leves)}")
