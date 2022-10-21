'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
inicio, fim, e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1;
b) de 10 até 0, de 2 em 2;
c) uma contagem personalizada.
'''
from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1
    else:
        p = p
    print('-=' * 20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p   
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
    print('FIM!')
    

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
