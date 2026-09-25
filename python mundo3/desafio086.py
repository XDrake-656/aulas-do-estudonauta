coluna1 = []
coluna2 = []
coluna3 = []
x= []
for linha in range(0,3):
    num = int(input(f"Digite um valor para a [0, {linha}]: "))
    coluna1.append(num)
x.append(coluna1)    
for linha in range(0,3):
    num = int(input(f"Digite um valor para a [1, {linha}]: "))
    coluna2.append(num)
x.append(coluna2)      
for linha in range(0,3):
    num = int(input(f"Digite um valor para a [2, {linha}]: "))
    coluna3.append(num)
x.append(coluna3)  
print("=-"*30)
for numeros in x:
    print(numeros)
