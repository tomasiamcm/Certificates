'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
'''
from interface import main
from cadastro import arquivo
from time import sleep

arq =  'base.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    opcao = main.menu(['Listar usuários', 'Cadastrar novo usuário', 'Sair'])
    if opcao == 1:
        arquivo.lerArquivo(arq)
    elif opcao == 2:
        main.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = main.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif opcao == 3:
        main.cabecalho('Saindo dd sistema... Até Logo!')
        break
    else:
        main.cabecalho('\033[31mERRO: Opção inválida. Tente novamente!\033[m')
    sleep(1)




