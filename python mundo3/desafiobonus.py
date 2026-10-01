from Dbonus.sistema import *
from Dbonus.arquivo import *
from time import sleep
arq = "cadastros.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)
login = False
while True:
    tabela(["criar conta", "Logar no sistema", "Sair do sistema"])
    opc = leiaInt(f"{cores(2)}Sua opção: {cores()}")
    if opc == 1:
        titulo("NOVO CADASTRO")
        nome = cadastraNome("NOME: ")
        sen = cadastrarSenha("SENHA: ")
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
