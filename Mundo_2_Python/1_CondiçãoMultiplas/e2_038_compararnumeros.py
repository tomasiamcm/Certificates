num1 = input('Informe um número: ')
num2 = input('Informe outro número: ')

if num1 > num2:
    print('O primeiro número: {} é maior que o segundo número: {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo número: {} é maior que o primeiro númeto: {}'.format(num2, num1))
else:
    print('Os dois números são iguais.')

