num1 = int(input('Digite um número: '))

# Calculando o Dobro
dobro = num1 * 2

# Calculando o Triplo
triplo = num1 * 3

# Calculando a raiz quadrada
# raiz = num1 / 1/2
raiz = pow(num1, 1/2)

print('O dobro de {} é: {}.'.format(num1, dobro))
print('O triplo de {} é: {}.'.format(num1, triplo))
print('A raiz quadrada de {} é: {:.2f}.'.format(num1, raiz))