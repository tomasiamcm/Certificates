'''
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Mostre a listagem dos números gerados e também o menor e o maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print('-=' * 20)
print(f'Os números sorteados foram: {numeros}')
print('-=' * 20)
print(f'O maior número foi {max(numeros)}')
print('-=' * 20)
print(f'O menor número foi: {min(numeros)}')