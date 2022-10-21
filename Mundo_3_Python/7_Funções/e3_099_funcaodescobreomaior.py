'''
Faça um programa que tenha uma função maior(), que receba vários parâmetros com números inteiros.
Analise todos os números e diga qual o maior número.
'''

from time import sleep

def maior(* numeros):
    cont = max = 0
    print('\nAnalisando os valores passados...')
    for n in numeros:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
 #       if cont == 0:
 #           max = n
 #       else:
        if n > max:
            max = n
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi de {max}.')
    print('-' * 25)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
