palavras = (
    "casa", "Cry", "carro", "Rhythm", "sol", 
    "Gym", "livro", "tst", "computador", "gng", 
    "arvore", "fly", "janela", "Myth", "escola"
            )
Vogais = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
for c in range(0, len(palavras)):
    print(f"\nNa palavra {palavras[c]} tem Quais vogais? ", end="")
    letras = list(palavras[c])
    vogal = False
    for letra in letras:
        if letra in Vogais:
            print(letra, end=" ")
            vogal = True
    if vogal == False:
        print("Não tem vogal!", end="")
