from time import sleep

from Dbonus.arquivo import *
from Dbonus.sistema import *

arq = "cadastros.txt"
if not arquivo_existe(arq):
    criar_arquivo(arq)
login = False
while True:
    tabela(["criar conta", "Logar no sistema", "Sair do sistema"])
    opc = leia_int(f"{cores(2)}Sua opção: {cores()}")
    if opc == 1:
        titulo("NOVO CADASTRO")
        nome = cadastra_nome("NOME: ")
        sen = cadastrar_senha("SENHA: ")
        cadastrar(arq, nome, sen)

    elif opc == 2:
        titulo("LOGAR NO SISTEMA")
        nome = input("NOME: ").strip()
        sen = input("SENHA: ").strip()
        if logar(arq, nome, sen):
            sleep(1)
            print(f"{cores(2)}BEM VINDO {nome}!{cores()}")
            break
        
    elif opc == 3:
        titulo("ENCERRANDO SISTEMA...")
        break
    
    else:
        print(f"{cores(1)}ERRO! Opção não valida.{cores()}")
        sleep(1)
