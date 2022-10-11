'''
Crie um programa que leia vários números e só pare quando digitar 999.
Mostre quantos números foram digitados e qual foi a soma entre eles.
'''
cont = soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
    
print(f'Você digitou {cont} números e a soma deles é {soma}.')
