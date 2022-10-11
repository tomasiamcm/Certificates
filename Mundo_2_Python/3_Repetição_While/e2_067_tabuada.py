'''
Crie um programa que calcula a tabuada de um número.
'''
print('=' * 30 + ' TABUADA ' + '=' * 30)

while True:
    print('-' * 70)
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
print('O número informado é negativo. Tente novamente!')