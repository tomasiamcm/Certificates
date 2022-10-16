'''
Crie uma tupla com preços e no final mostre a listagem de forma tabulada.
'''

from typing import ItemsView


tabela = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(tabela)):
    if item % 2 == 0:
        print(f'{tabela[item]:.<30}', end='')
    else:
        print(f'R$ {tabela[item]:>7.2f}')