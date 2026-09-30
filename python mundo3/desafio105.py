def notas(*nota, sit = False):
    """ => Função para analisar notas e situações de vrios alunos.
    :parametro n: uma ou mais notas
    :parametro sit: valor opcional indicando se de ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    n ={}
    n["total"] = len(nota)
    n["maior"] = max(nota)
    n["menor"] = min(nota)
    n["media"] = round(sum(nota)/len(nota),2)
    if sit == True:
        if n["media"] < 6.00:
            n["situação"] = "RUIM"
        elif n["media"] < 7.00:
            n["situação"] = "RAZOAVEL"
        else:
            n["situação"] = "BOA"
    return n

resp = notas(5.5, 2, 6, 6.5, 10, 9, 8, sit = True)
print(resp)
