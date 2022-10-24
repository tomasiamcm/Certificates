'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas:
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é R$ {moeda.dobro(p)}')
print(f'O valor de {p} acrescido de 10% é de R$ {moeda.aumentar(p, 10)}')
print(f'O valor de {p} reduzido de 13% é de R$ {moeda.diminuir(p, 13)}')
