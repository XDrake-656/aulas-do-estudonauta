def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")

soma(4, 5)
soma(8, 9)
soma(8, 1)
soma(b= 4, a=5)

def contador(*num):
    print(f"recebi os valores {num} e são ao todo {len(num)} numeros")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,2,9,1,0,2]
print(valores)
dobra(valores)
print(valores)

def multiplica(*valores):
    mult = 1
    for num in valores:
        mult *= num
    print(f"A multiplicacao dos valores {valores} é igual a {mult}")

multiplica(3, 4)
multiplica(2,6,9)
multiplica(2,8,6,7,12)
