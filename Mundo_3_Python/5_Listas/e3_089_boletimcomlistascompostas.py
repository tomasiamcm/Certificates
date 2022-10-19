'''
Crie um programa que leia nome e 2 notas de vários alunos, guarde-os em lista.
a) Mostre um boletim com a média de cada aluno;
b) permita que o usuário possa ver as notas de cada aluno individualmente.
'''

caderneta = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input(f'Informe a 1ª nota: '))
    nota2 = float(input(f'Informe a 2ª nota: '))
    media = (nota1 + nota2) / 2
    caderneta.append([nome, [nota1, nota2], media])
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 25)
for i, a in enumerate(caderneta):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 15)
    opc = int(input('Informe o código do aluno que deseja ver as ntoas? (999 para finalizar) '))
    if opc <= len(caderneta) - 1:
        print(f'{caderneta[opc][0]} tirou as notas {caderneta[opc][1]}')
    if opc == 999:
        print('FINALIZANDO...')
        break        
print('<<< VOLTE SEMPRE >>>')
