# Faça um programa que leia o peso de 5 pessoas e no final mostre o maior e o menor peso lido.
maior_peso = 0
menor_peso = 0

for n in range(1,6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(n)))
    if n == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi de {} Kg e o menor peso foi de {} Kg.'.format(maior_peso, menor_peso))        

