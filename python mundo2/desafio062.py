primeiro=int(input("Digite o primeiro termo da PA : "))
razao=int(input("Digite a razão da PA: "))
print(f"A pa dos numero {primeiro} com a razão de {razao} é:")
numeros = 0
termos = 10
while numeros != termos:
    pa = primeiro + (numeros * razao)
    numeros += 1
    print(pa, end=", ")
    if numeros == termos:
        print(".....")
        mais = int(input("\nesses foram os 10 primeiros termos, voce quer mais quantos termos dessa pa (digite 0 se quiser mais)"))
        if mais == 0:
            print(f"esses foram os {termos} termos dessa pa.")
        else:
            termos += mais
print("FIM!")
