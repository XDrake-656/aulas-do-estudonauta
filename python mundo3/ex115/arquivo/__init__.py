from ex115.sistema import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print(f"{cores(1)}Houve um ERRO na criação do arquivo!{cores()}")
    else:
        print(f"{cores(2)}arquivo {nome} criado com sucesso!{cores()}")

def leiaArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print(f"{cores(1)}Houve um ERRO ao tentar ler o arquivo!{cores()}")
    else:
        titulo("PESSOAS CADASTRADAS")
        for linha in a:
            pessoa = linha.split(":")
            pessoa[1] = pessoa[1].replace("\n", "")
            print(f"{pessoa[0]:<30}{pessoa[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome="Desconhecido", idade="desconhecida"):
    try:
        a = open(arq, "at")
    except:
        print(f"{cores(1)}Houve um ERRO ao tentar abrir o arquivo!{cores()}")
    else:
        try:
            a.write(f"{nome}:{idade}\n")
        except:
            print(f"{cores(1)}Houve um ERRO ao tentar cadastrar o(a) {nome}!{cores()}")
        else:
            print(f"{cores(2)}{nome} cadastrado(a) com sucesso!{cores()}")
            a.close()
