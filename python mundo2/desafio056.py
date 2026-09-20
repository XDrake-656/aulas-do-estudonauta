grupo = 0
nomev = ""
velho = 0
mulnova = 0
for g in range(1,5):
    nome = str(input(f"Pessoa {g}. Qual é seu nome? ")).strip().title()
    idade = int(input(f"Pessoa {g}. Qual a sua idade? "))
    sexo = int(input(f"Pessoa {g}. Qual é seu sexo?(digite 1 para 'MASCULINO' ou 2 para 'FEMININO') "))
    grupo += idade
    
    if g == 1 and sexo == 1:
        velho = idade
        nomev = nome
    elif sexo == 1: 
        if velho < idade:
            velho = idade
            nomev = nome
            
    if sexo == 2 and idade < 20:
        mulnova = mulnova + 1
        
print(f"A media de idade desse grupo é de {grupo/4:.1f}.")
print(f"O homem  mais velho se chama {nomev} e ele tem {velho} anos de idade.")
print(f"E neste grupo tem {mulnova} mulheres com menos de 20 anos de idade.")
