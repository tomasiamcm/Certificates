nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Você está reprovado!')
elif media < 6.9:
    print('Você está em recuperação.')
else:
    print('Você está aprovado.')

print('Sua média foi {}'.format(media))