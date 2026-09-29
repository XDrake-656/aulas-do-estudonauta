def notas(*nota, sit = False):
    """ => Função para analisar notas e situações de vrios alunos.
    :parametro n: uma ou mais notas
    :parametro sit: valor opcional indicando se de ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    n ={}
    medias = 0
    n["total"] = len(nota)
    n["maior"] = max(nota)
    n["menor"] = min(nota)
    for c in range(len(nota)):
        medias += nota[c]
    media_total = round((medias/len(nota)),2)
    n["media"] = media_total
    if sit == True:
        if media_total < 6:
            n["situação"] = "RUIM"
        elif media_total < 7:
            n["situação"] = "RAZOAVEL"
        else:
            n["situação"] = "BOA"
    return n

resp = notas(5.5, 2, 6, 6.5, 10, 9, 8, sit = True)
print(resp)
