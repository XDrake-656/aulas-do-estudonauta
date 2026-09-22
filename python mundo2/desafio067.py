while True:
    num = int(input("Você quer a tabuada de qual valor? "))
    if num < 0:
            break
    print("=+="*20)
    for t in range(1, 11):
        print(f"|{num:3} X {t:3} = {num*t:3}|")
    print("=+="*20)
    
print("fim")    
