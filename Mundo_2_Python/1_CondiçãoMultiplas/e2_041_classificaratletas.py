from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print('O atleta tem {} anos.'.format(idade))

if idade < 9:
    print('Classificação: Mirim')
elif idade < 14:
    print('Classificação: Infantil')
elif idade < 19:
    print('Classificação: Júnior')
elif idade < 20:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')

