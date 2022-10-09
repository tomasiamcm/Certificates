idade = int(input('Informe a idade: '))

if idade < 9:
    print('')
elif idade < 14:
    print('Infantil')
elif idade < 19:
    print('Júnior')
elif idade < 20:
    print('Sênior')
else:
    print('Master')

