def leiaDinheiro(txt):
    while True:
        n = input(txt).strip().replace(",",".")
        if n.isnumeric() or ("." in n and n.isnumeric):
            return float(n)
        else:
            print(f"\033[0;31mERRO! '{n}' é um valor inavlido!\033[m")
