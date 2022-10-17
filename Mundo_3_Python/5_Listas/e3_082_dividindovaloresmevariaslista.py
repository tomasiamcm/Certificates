'''
Crie um programa que receba vários números e coloque-os em uma lista.
Depois, crie 2 outras listas, sendo uma para números pares e outra
para números impares.
Mostre as 3 listas
'''

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
print('-=' * 30)
print(f'A lista completa é: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
