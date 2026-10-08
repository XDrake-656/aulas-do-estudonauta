# noqa: N999
from ..sistema import *


def arquivo_existe(nome):
    try:
        with open(nome, "rt"):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        with open(nome, "wt+"):
            pass
    except FileExistsError:
        print(f"{cores(1)}ERRO! Não foi possivel criar o arquivo {nome}{cores()}")
    else:
        print(f"{cores(2)}arquivo {nome} criado com sucesso!{cores()}")


def leia_arquivo(nome):
    lista = []
    try:
        with open(nome, "rt") as a:
            usuario = {}
            for linha in a:
                cadastro = linha.split(":")
                cadastro[1] = cadastro[1].replace("\n", "")
                usuario["nome"] = cadastro[0]
                usuario["senha"] = cadastro[1]
                lista.append(usuario.copy())
    except FileNotFoundError:
        print(f"{cores(1)}Houve um ERRO. Arquivo não encontrado!{cores()}")
    except PermissionError:
        print(f"{cores(1)}Houve um ERRO. Você não tem permissão para acessesar esse arquivo!{cores()}")
    except IsADirectoryError:
        print(f"{cores(1)}Houve um ERRO. Tentando abrir um diretorio tente apenas arquivo!{cores()}")
    except UnicodeDecodeError:
        print(f"{cores(1)}Houve um ERRO. Usando codificação inconpativel!{cores()}")
    return lista


def cadastra_nome(txt):
    try:
        lista = leia_arquivo("cadastros.txt")
    except FileNotFoundError:
        print(f"{cores(1)}Houve um ERRO. Arquivo não encontrado!{cores()}")
    except PermissionError:
        print(f"{cores(1)}Houve um ERRO. Você não tem permissão para acessesar esse arquivo!{cores()}")
    except IsADirectoryError:
        print(f"{cores(1)}Houve um ERRO. Tentando abrir um diretorio tente apenas arquivo!{cores()}")
    except UnicodeDecodeError:
        print(f"{cores(1)}Houve um ERRO. Usando codificação inconpativel!{cores()}")
    else:
        while True:
            invalidos = r""" +=\$%<>*@#!?^&|/"'`"""
            print("digite seu nome. Usar apenas letras (A-Z), números (0-9) e underline (_) ou hífen (-) e não use espaços.")
            nome = input(txt).strip()
            if nome == "" or any(caractere in nome for caractere in invalidos):
                print(f"{cores(1)}ERRO! Nome invalido{cores()}")
            else:
                for usuario in lista:
                    if usuario["nome"] == nome:
                        print(f"{cores(1)}ERRO! Nome ja cadastrado{cores()}")
                        break
                else:
                    print(f"{cores(2)}Nome disponivel!{cores()}")
                    break
        return nome


def cadastrar(arq, nome, senha):
    try:
        with open(arq, "at") as a:
            a.write(f"{nome}:{senha}\n")
    except FileNotFoundError:
        print(f"{cores(1)}Houve um ERRO. Arquivo não encontrado!{cores()}")
    except PermissionError:
        print(f"{cores(1)}Houve um ERRO. Você não tem permissão para acessesar esse arquivo!{cores()}")
    except IsADirectoryError:
        print(f"{cores(1)}Houve um ERRO. Tentando abrir um diretorio tente apenas arquivo!{cores()}")
    except UnicodeDecodeError:
        print(f"{cores(1)}Houve um ERRO. Usando codificação inconpativel!{cores()}")
    else:
        print(f"{cores(2)}{nome} cadastrado(a) com sucesso!{cores()}")


def logar(arq, nome, senha):
    try:
        lista = leia_arquivo(arq)
    except FileNotFoundError:
        print(f"{cores(1)}Houve um ERRO. Arquivo não encontrado!{cores()}")
    except PermissionError:
        print(f"{cores(1)}Houve um ERRO. Você não tem permissão para acessesar esse arquivo!{cores()}")
    except IsADirectoryError:
        print(f"{cores(1)}Houve um ERRO. Tentando abrir um diretorio tente apenas arquivo!{cores()}")
    except UnicodeDecodeError:
        print(f"{cores(1)}Houve um ERRO. Usando codificação inconpativel!{cores()}")
    else:
        for usuario in lista:
            if usuario["nome"] == nome and usuario["senha"] == senha:
                print(f"{cores(2)}Login realizado com sucesso!{cores()}")
                return True
        print(f"{cores(1)}ERRO! Nome ou senha incorretos.{cores()}")
        return False
