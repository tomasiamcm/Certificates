'''
Desenvolva um programa que leia 4 valores e guarde-os em uma tupla. No final, mostre:
a) quantas vezes apareceu o valor 9;
b) em que posição foi digitado o 1º valor 3;
c) quais foram os números pares;
'''

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
            int(input('Digite outro número: ')), int(input('Digite outro número: ')))
print('-=' * 20)
print(f'Você digitou os números: {numeros}')
print('-=' * 20)
if 9 in numeros:
    print(f'O número 9 apareceu: {numeros.count(9)} vezes.')
else:
    print(f'O número 9 não foi digitado.')
print('-=' * 20),
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição.')
else:
    print(f'O número 3 não foi digitado.')
print('-=' * 20)
print(f'Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')