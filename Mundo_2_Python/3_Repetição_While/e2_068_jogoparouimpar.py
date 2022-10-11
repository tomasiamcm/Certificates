'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder.
Mostrando o total de vitórias consecutivas.
'''
from random import randint

print('=' * 30 + ' PAR ou ÍMPAR? ' + '=' * 30)
cont = 0

while True:
    jogador = int(input(('Digite um número: ')))
    computador = randint(0, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}, total {soma}.')
    #print('Deu PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Deu PAR, você VENCEU!')
            cont += 1
        else:
             print('Deu ÍMPAR, você PERDEU!')
             break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Deu ÍMPAR, você VENCEU!')
            cont += 1
        else:
             print('Deu PAR, você PERDEU!')
             break
    print('Vamos jogar novamente...')

if cont == 0:
    print(f'GAME OVER!!!!! Você ganhou nenhuma vez.')
else:    
    print(f'GAME OVER!!!!! Você venceu {cont} vezes.')