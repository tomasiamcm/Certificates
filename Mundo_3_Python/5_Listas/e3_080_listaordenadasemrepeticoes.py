'''
Crie um programa que receba 5 números e coloque-os em uma lista, já na posição correta de inserção
(sem usar o sort()).
No final mostre a lista ordenada.
'''

lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O número foi adicionado na posição {c} da lista.')
    else:
        posicao = 0  
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
        print(f'O número {n} foi adicionado na posição {posicao} da lista.')
print('-=' * 30)
print(f'Os números digitados em ordem crescente é: {lista}')