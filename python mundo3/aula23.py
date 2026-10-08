try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    c = a/b
    
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dadso que voce digitou.")
except ZeroDivisionError:
    print("Não é possivel dividir um numero por zero!")
except KeyboardInterrupt:
    print("O usario preferriu não informar os dados")
except Exception as erro:
    print(f"o erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {c:.1f}")
finally:
    print("Volte sempre! Muito obrigado!")
