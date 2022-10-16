'''
Escreva um programa que leia um número e escreva seu valor por extenso.
'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[]}.')
