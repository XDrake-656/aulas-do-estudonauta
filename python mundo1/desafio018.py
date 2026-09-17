from math import radians, sin, cos, tan
an=float(input("Digite um angulo: "))
x=radians(an)
print("O seno conseno e a tangente de {:.2f} são respectivamente {:.2f}, {:.2f} e {:.2f}".format(an,sin(x),cos(x),tan(x)))
 