'''
Crie um programa que leia nome e 2 notas de vários alunos, guarde-os em lista.
a) Mostre um boletim com a média de cada aluno;
b) permita que o usuário possa ver as notas de cada aluno individualmente.
'''

boletim = []
nome = []
notas = [nome[:]]


while True:
    nome.append(str(input('Nome: ')))
    nota

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]'))
        if continua == 'N':
            break
