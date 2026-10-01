from ex115.sistema import *
from ex115.arquivo import *
from time import sleep
arq = "pessoascadastradas.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    tabela(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    opc = leiaInt(f"{cores(2)}Sua opção: {cores()}")
    if opc == 1:
        leiaArquivo(arq)

    elif opc == 2:
        titulo("NOVO CADASTRO")
        nome = input("NOME: ").strip().title()
        idade = leiaInt("IDADE: ")
        cadastrar(arq, nome, idade)
        
    elif opc == 3:
        titulo("ENCERRANDO SISTEMA...")
        break
    
    else:
        print(f"{cores(1)}ERRO! Opção não valida.{cores()}")
        sleep(1)
