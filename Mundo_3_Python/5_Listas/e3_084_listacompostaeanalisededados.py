'''
Crie um programa que leia nome e peso de várias pessoas e coloque em uma lista.
NO final, mostre:
a) quantas pessoas foram cadastradas;
b) listagem com as pessoas mais pesadas;
c) listagem com as pessoas mais leves.
'''

lista = []
digitacao = []
max = min = 0

while True:
    digitacao.append(str(input('Informe o nome: ')))
    digitacao.append(float(input('Informe o peso: ')))
    if len(lista) == 0:
        max = min = digitacao[1]
    else:
        if digitacao[1] > max:
            max = digitacao[1]
        if digitacao[1] < min:
            min = digitacao[1]
    lista.append(digitacao[:])
    digitacao.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? ')).upper().strip()[0]
    if continua == 'N':
        break

print('-=' * 30)
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {max} Kg. Peso de ', end='')
for p in lista:
    if p[1] == max:
        print(f'[{p[0]}] .', end='')
print()
print(f'O menor peso foi de {min} Kg. Peso de ', end='')
for p in lista:
    if p[1] == min:
        print(f'[{p[0]}] .', end='')