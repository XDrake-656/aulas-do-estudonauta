num = int(input("qual numero que voce deseje o seu fatorial: "))
fatorial = 1
final = 1

while fatorial != num:
    fatorial = fatorial + 1
    print(f"X {fatorial}", end=" ")
    final = fatorial * final

print(f"\nA fatorial de {num} é {final}")    
print("fim")

"""
final = 1
for f in range(1 , num + 1):
    print(f)
    final = f * final
print(f"\nA fatorial de {num} é {final}")    
print("fim")
"""