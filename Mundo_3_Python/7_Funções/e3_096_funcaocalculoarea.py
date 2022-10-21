'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''

def area(a, b):
    area = a * b
    print(f'A área de um terreno de {a}m de largura X {b}m de comprimento é de {area}m².')


print(' Controle de Terrenos ')
print('-' * 25)
a = float(input('Informe a largura do terreno (m): '))
b = float(input('Informe o comprimento do terreno(m): '))
area(a, b)

