'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
n = int(input('Digite um número (999 para parar): '))
soma = cont = 0

while n != 999:
    soma += n
    cont += 1
    n = int(input('Informe outro número (999 para parar): '))
print('Fim. Você digitou {} números e a soma deles é {}.'.format(cont, soma))

