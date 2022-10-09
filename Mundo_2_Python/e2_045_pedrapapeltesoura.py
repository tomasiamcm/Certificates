# Jokenpô
import random
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Escolha sua opção: 
[0] Pedra
[1] Papel
[2] Tesoura
''')

jogador = int(input('Qual a sua jogada? '))

if jogador < 0 or jogador > 2:
    print('Opção inválida. Tente novamnete!')
else: 
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)

    print('-=' * 10)
    print('Computador jogou {}'.format(lista[computador]))
    print('Jogador jogou {}'.format(lista[jogador]))
    print('-=' * 10)
    if computador == 0: # Pedra
        if jogador == 0: # Pedra
            print('Deu empate, você escolheu a mesma opção do computador.')
        elif jogador == 1: # Papel
            print('Você ganhou! O papel embrulha a pedra.')
        else: # Tesoura
            print('Você perdeu! A pedra quebra a tesoura.')

    if computador == 1: # Papel
        if jogador == 0: # Pedra
            print('Você perdeu! O papel embrulha a pedra.')
        elif jogador == 1: # Papel
            print('Deu empate, você escolheu a mesma opção do computador.')
        else: # Tesoura
            print('Você ganhou! A tesoura corta o papel.')
    
    if computador == 2: # Tesoura
        if jogador == 0: # Pedra
            print('Você ganhou! A pedra quebra a tesoura.')
        elif jogador == 1: # Papel
            print('Você perdeu! A tesoura corta o papel.')
        else: # Tesoura
            print('Deu empate, você escolheu a mesma opção do computador.')
