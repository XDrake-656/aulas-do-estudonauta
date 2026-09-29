def maior(*num):
    print("-=" * 25)
    if len(num) >= 1:
        print(f"Analizando os valores passodos...\n{" ".join(map(str, num))} Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {max(num)}.")
    else:
        print(f"Analizando os valores passodos...{" ".join(num)}\nForam informados {len(num)} valores.")

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
