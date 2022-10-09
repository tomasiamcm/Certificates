from datetime import date

ano = int(input('Informe o ano de nascimento: '))
idade = date.today(year) - ano
idade_alistamento = 18

if idade < idade_alistamento:
    resultado = (idade - idade_alistamento) * -1
    print('Faltam {} anos para o alistamento militar.')
elif idade == idade_alistamento:
    print('Você está na idade do alistamento militar.')
else:
    resultado = (idade - idade_alistamento)
    print('Já passou o prazo para alistamento militar.')
