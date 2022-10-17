'''
Crie um programa que lê vários números e coloca em uma lista. Mostre:
a) quantos números foram digitados;
b) a lista de valores em ordem decrescente;
c) se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
print('-=' * 30)
print(f'Os números da lista são: {lista}')
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista com os números em ordem decrescente é: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')