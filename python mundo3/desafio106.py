def pyhelp():
    from time import sleep
    def titulos(txt):
        print("~" * (len(txt) + 2))
        print(f" {txt} ")
        print("~" * (len(txt) + 2))

    def cores(cor = ""):
        if cor in "Rr":
            print("\033[1;37;41m")
        if cor in "Gg":
            print("\033[1;37;42m")
        if cor in "Bb":
            print("\033[1;37;44m")
        if cor in "Ww":
            print("\033[7;37;47m")
        if cor in "Ll":
            print("\033[k\033[m")

    while True:
        cores("G")
        titulos("SISTEMA DE AJUDA PYHELP")
        cores("L")
        perg = input("Função ou Biblioteca => ")
        if perg == "Fim" or perg == "fim":
                    cores("R")
                    titulos("ATÉ LOGO!")
                    cores("L")
                    break
    
        cores("B")
        titulos(f"Acessando o manual do comando '{perg}'")
        sleep(2)
        cores("L")
        cores("W")
        help(perg)
        cores("L")

pyhelp()