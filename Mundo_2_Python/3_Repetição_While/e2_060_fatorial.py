num = int(input('Digite um númeropara calcular o seu fatorial: '))
cont = num
fatorial = 1
print('Calculando {}! => '.format(num), end='')

while cont > 0:
    print('{}'.format(cont),end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -=1

print('{}'.format(fatorial))

###################### Ourta Forma ##############################
'''
from math import factorialpara calcular o seu fatorial:

n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
'''
