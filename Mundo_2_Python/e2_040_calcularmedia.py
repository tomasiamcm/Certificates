nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f} a média é {:.1f}.'.format(nota1, nota2, media))

if media < 5:
    print('Você está reprovado!')
elif media < 6.9:
    print('Você está em recuperação.')
else:
    print('Você está aprovado.')
