'''
Crie u =m programa que receba vários números e coloque-os em uma lista, sem repeti-los.
No final, mostre todos os números em ordem crescente.
'''

lista = []

while True:
    n = int(input('Informe um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break

print('-' * 30)
print(lista)
lista.sort()
print(lista)
