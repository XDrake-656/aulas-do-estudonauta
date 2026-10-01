from Dbonus.sistema import *
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
        print(f"{cores(1)}ERRO! Não foi possivel criar o arquivo {nome}{cores()}")
    else:
        print(f"{cores(2)}arquivo {nome} criado com sucesso!{cores()}")

def leiaArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print(f"{cores(1)}Houve um ERRO ao tentar ler o arquivo!{cores()}")
    else:
        usuario = {}
        lista = []
        for linha in a:
            cadastro = linha.split(":")
            cadastro[1] = cadastro[1].replace("\n", "")
            usuario["nome"] = cadastro[0]
            usuario["senha"] = cadastro[1]
            lista.append(usuario.copy())

    finally:
        a.close()
    return lista

def cadastraNome(txt):
    try:
        lista = leiaArquivo("cadastros.txt")
    except:
        print(f"{cores(1)}Houve um ERRO ao tentar ler o arquivo!{cores()}")
    else:
        while True:
            nome = input(txt).strip()
            if nome == "":
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
        a = open(arq, "at")
    except:
        print(f"{cores(1)}Houve um ERRO ao tentar abrir o arquivo!{cores()}")
    else:
        try:
            a.write(f"{nome}:{senha}\n")
        except:
            print(f"{cores(1)}Houve um ERRO ao tentar cadastrar o(a) {nome}!{cores()}")
        else:
            print(f"{cores(2)}{nome} cadastrado(a) com sucesso!{cores()}")
            a.close()

def logar(arq, nome, senha):
    try:
        lista = leiaArquivo(arq)
    except:
        print(f"{cores(1)}Houve um ERRO ao tentar ler o arquivo!{cores()}")
    else:
        for usuario in lista:
            if usuario["nome"] == nome and usuario["senha"] == senha:
                print(f"{cores(2)}Login realizado com sucesso!{cores()}")
                return True
        else:
            print(f"{cores(1)}ERRO! Nome ou senha incorretos.{cores()}")
            return False
