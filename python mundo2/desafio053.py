f=str(input("Escreva uma frase: ")).strip().upper().replace(",", "").replace("-","")
palavras = f.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]

print(f"voce digitou a frase {f}.")
print(f"esta frase invertida fica {inverso}.")
if junto == inverso:
    print("esta frase é um polindromo")
else:
    print("esta frase não é um polindromo")

# alternativa ao inves de usar o for (inverso = junto[::-1])
"""
f=str(input("Escreva uma frase: ")).strip().upper().replace(",", "").replace("-","")
palavras = f.split()
junto = "".join(palavras)
inverso = junto[::-1]
print(f"voce digitou a frase {f}.")
print(f"esta frase invertida fica {inverso}.")
if junto == inverso:
    print("esta frase é um polindromo")
else:
    print("esta frase não é um polindromo")
"""
