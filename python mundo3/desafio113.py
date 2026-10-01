def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print("\033[1;31mERRO! Por favor, digite um numero inteiro valido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mUsuario preferiu não informar os numeros.\033[m")
            return 0
        else:
            return num

def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt).replace(",", "."))
        except (ValueError, TypeError):
            print("\033[1;31mERRO! Por favor, digite um numero real valido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mUsuario preferiu não informar os numeros.\033[m")
            return 0
        else:
            return num

i = leiaInt("Digite um numero inteiro: ")
f = leiaFloat("Digite um numero real: ")
print(f"Você digitou o numero inteiro {i} e o numero real {f}")
