'''
Faça um programa que ajude um jogador a criar palpites para mega sena.
Deve perguntar quantos jogos;
Sortear 6 números e não repeti-los no mesmo jogo.
'''
from time import sleep
from random import randint

print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)

lista = []
jogos = []

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 5, f' SORTEANDO {quantidade} JOGOS ', '=-' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 6, '< BOA SORTE! >', '=-' * 6)




