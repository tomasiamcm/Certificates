'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
max_coluna2 = soma_pares = soma_coluna3 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Informe um número para a {linha + 1}ª linha e {coluna + 1}ª coluna: '))

print('-=' * 30)
print(matriz)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é: {soma_pares}')

for linha in range(0, 3):
    soma_coluna3 += matriz[linha][2]
print(f'A soma da 3ª coluna é: {soma_coluna3}')

for coluna in range(0, 3):
    if coluna == 0:
        max_coluna2 = matriz[1][coluna]
    elif matriz[1][coluna] > max_coluna2:
        max_coluna2 = matriz[1][coluna]
print(f'O maior valor da 2ª linha é: {max_coluna2}')
