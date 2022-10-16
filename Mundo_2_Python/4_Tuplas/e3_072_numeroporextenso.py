'''
Escreva um programa que leia um número e escreva seu valor por extenso.
'''

extenso = (0,'zero', 1,'um', 2, 'dois', 3, 'três', 4, 'quatro', 5, 'cinco', 6, 'seis', 7, 'sete', 8, 'oito',
            9, 'nove', 10, 'dez', 11, 'onze', 12, 'doze', 13, 'treze', 14, 'quatorze', 15, 'dezeseis',
            17, 'dezessete', 18, 'dezoito', 19, 'dezenove', 20, 'vinte')
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Informe um número entre 0 e 20: '))
    else:
        print(num)
        break

