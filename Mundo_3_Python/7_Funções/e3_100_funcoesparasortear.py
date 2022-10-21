'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep

def sorteia(* numero):
    print('-=' * 20)
    print(f'Sorteando {n} números: ', end='')
    sleep(0.3)
    for cont in range(0, n):
        num = randint(0, 50)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(numero):
    total_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            total_pares += numero
    print(f'A soma dos números pares sorteados dá {total_pares}.') 

# Programa Principal
lista = []
n = int(input('QUantos números deseja sortear? '))
sorteia(lista)
somaPar(lista)


