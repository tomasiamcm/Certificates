'''
Escreva um programa que leia um número e escreva seu valor por extenso.
'''

extenso = ('0:zero', '1:um')
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Informe um número entre 0 e 20: '))
    else:
        print(num)
        break

