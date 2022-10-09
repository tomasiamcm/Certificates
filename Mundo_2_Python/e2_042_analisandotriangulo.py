print('-=-'*20)
print('Analisandr de Trinagulos')
print('-='*20)

r1 = float(input('Informe o tamanho da 1ª reta: '))
r2 = float(input('Informe o tamanho da 2ª reta: '))
r3 = float(input('Informe o tamanho da 3ª reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo.')
    if r1 == r2 == r3:
        print('É um triângulo Equilátero')
    elif r1 != r2 != r3:
        print('É um triângulo Escaleno')
    else:
        print('É um triângulo Isósceles')
else:
    print('Não é possível formar um triângulo.')


