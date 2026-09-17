n1=int(input("digite um numero:"))
n2=int(input("digite outro numero:"))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
rd=n1%n2
p=n1**n2
print("as operações entre os números {} e {} são: \n a soma é {} \n a multiplicação é {} \n a potencia é {} \n a divisão é {:.3f} \n a divisão inteira é {} \n e o resto da divisão é {}".format(n1,n2,s,m,p,d,di,rd))
