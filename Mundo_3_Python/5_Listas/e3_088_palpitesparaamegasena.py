'''
Faça um programa que ajude um jogador a criar palpites para mega sena.
Deve perguntar quantos jogos;
Sortear 6 números


'''
from time import sleep
from random import randint

print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)

jogos = []

n = int(input('Quantos jogos você quer que eu sorteie? '))

for n in range(0, n):
    for c in range(0, 6):
        jogos.append([randint(1, 61)])
        print(f'-=' * 3 + ' SORTEANDO {n} JOGOS ' + '-=' * 3)
        sleep(5)
print(jogos)
