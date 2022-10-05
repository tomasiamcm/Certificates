num = int(input('Informe um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A Unidade do número {} é {}.'.format(num, u))
print('A Dezena do número {} é {}.'.format(num, d))
print('A Centena do número {} é {}.'.format(num, c))
print('A Milhar do número {} é {}.'.format(num, m))




