'''
import random

num = input('Informe um número entre 0 e 5: ' )

lista = ['0', '1', '2', '3', '4']


if num == random.choice(lista):
    print('Você acertou!')
else:
    print("Você não acertou. Tente novamente!")
'''


#####################       Outra forma          #######################
''''''
from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = input('Informe seu número: ' )
print('Processando...')
sleep(3)

if jogador == computador:
    print('Parabéns! Você acertou.')
else:
    print('Você errou. Eu pensei no número {} e você no {}!'.format(computador, jogador))
