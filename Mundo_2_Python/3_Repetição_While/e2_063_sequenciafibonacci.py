# Criar um programa que leia um número inteiro e mostre o 'x' primeiros elementos de a sequência de fibonacci

from ast import Num

print('-=' * 20)
print('Gerador de Fibonacci')
print('-=' * 20)

n = int(input('Informe quantos termos você deseja: '))

t1 = 0
t2 = 1

print('-=' * 20)
print('{} -> {}'.format(t1, t2), end='')

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('-=' * 20)