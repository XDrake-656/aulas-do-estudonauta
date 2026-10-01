def cores(cor=0):
    if cor == 0:
        return "\033[m"#limpa
    if cor == 1:
        return "\033[1;31m"#vermelho
    if cor == 2:
        return "\033[1;32m"#verde
    if cor == 3:
        return "\033[1;33m"#amarelo
    if cor == 4:
        return "\033[1;34m"#azul

def titulo(txt):
    print("=" * 40)
    print(f"{txt:^40}")
    print("=" * 40)

def tabela(lista):
    titulo("MENU PRINCIPAL")
    for c in range(len(lista)):
        print(f"{cores(3)}{c + 1}{cores()} => {cores(4)}{lista[c]}{cores()}")
    print("=" * 40)

def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f"{cores(1)}ERRO! Por favor, digite um numero inteiro valido.{cores()}")
            continue
        except KeyboardInterrupt:
            print(f"{cores(1)}Usuario preferiu não informar os numeros.{cores()}")
            continue
        else:
            return num
