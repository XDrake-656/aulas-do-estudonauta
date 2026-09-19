n1=float(input("Escreva sua primeira nota: "))
n2=float(input("Escreva sua segunda nota: "))
media = (n1+n2)/2
if media < 5:
    print(f"A sua media é de {media:.1f}. \033[1;31mREPROVADO\033[m")
elif media >= 5 and media <= 6.9:
    print(f"A sua media é de {media:.1f}. \033[1;34mRECUPERAÇAO\033[m")
else:
    print(f"A sua media é de {media:.1f}. \033[1;32mAPROVADO\033[m")
