from datetime import date
n=int(input("em que ano você nasceu? "))
i=(n-(date.today().year))*-1
if i > 18:
    print(f"Como você tem {i} anos ja passou da hora de se alistar.")
    print(f"seu alistamento foi no ano de {date.today().year+(18-i)}")
elif i < 18:
    print(f"Como você tem {i} anos ainda faltam {18-i} anos para se alistar.")
    print(f"seu alistamento sera no ano de {(18-i)+date.today().year}")
else:
    print(f"Como você tem exatos {i} anos esta na hora de você se alistar.")
