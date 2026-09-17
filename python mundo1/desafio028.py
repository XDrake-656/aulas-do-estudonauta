from random import randint
r=randint(0,5)
n=int(input("Tente adivinhar o número que estou pensando entre 0 e 5:"))
if n==r:
    print("Parabéns! Você acertou!")
else:
    print("Você errou! Eu pensei no número {}.".format(r))
