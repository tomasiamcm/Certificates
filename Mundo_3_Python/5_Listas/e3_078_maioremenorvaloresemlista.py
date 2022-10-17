'''
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
Mostre:
a) maior valor e sua posição na lista
b) menor valor e sua posição na lista
'''

lista = []
max = 0
min = 0

for c in range(0, 5):
    lista.append(int(input(f'Informe um número para a posição {c}: ')))
    if c == 0:
        max = min = lista[c]
    else:
        if lista[c] > max:
            max = lista[c]
        if lista[c] < min:
            min = lista[c]

print('-' * 30)
print(f'A lista completa é: {lista}')
print(f'O maior número da lista é: {max} e está na posição: ', end='')
for i, v in enumerate(lista):
    if v == max:
       print(f'{i}... ', end='')
print()
print(f'O menor número da lista é: {min} e está na posição: ', end='')
for i, v in enumerate(lista):
    if v == min:
        print(f'{i}... ', end='')
print()
