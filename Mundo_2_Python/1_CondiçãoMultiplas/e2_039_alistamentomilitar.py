from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade =  ano_atual - ano_nascimento
idade_alistamento = 18

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
if idade == idade_alistamento:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < idade_alistamento:
    resultado = (idade - idade_alistamento) * -1
    print('Faltam {} anos para o alistamento militar.'.format(resultado))
else:
    resultado = (idade - idade_alistamento)
    print('Você já deveria ter se alistado há {} anos.'.format(resultado))
