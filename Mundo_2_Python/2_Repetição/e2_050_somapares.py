# Ler 6 números inteiros e mostre a soma dos valores pares.

soma = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares e a soma é {}.'.format(cont, soma))
