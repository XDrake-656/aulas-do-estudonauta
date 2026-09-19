from datetime import date
a=int(input("Em que ano você nasceu? "))
i=(date.today().year)-a
if i <= 9:
    print(f"Com {i} anos você é da categoria mirim.")
elif i <= 14:
    print(f"Com {i} anos você é da categoria infanti.")
elif i <= 19:
    print(f"Com {i} anos você é da categoria junior.")
elif i == 25:
    print(f"Com {i} anos você é da categoria sênior.")
else:
    print(f"Com {i} anos você é da categoria master.")
