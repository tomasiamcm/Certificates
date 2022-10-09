valor_casa = float(input('Informe o valor da casa a ser financiada: '))
valor_salario = float(input('Informe o valor do seu salário: '))

anos = int(input('INforme em quantos anos deseja pagar o financeiamento: '))

valor_prestacao = valor_casa / (anos*12)
limite_parcela = valor_salario * (30 / 100)


if valor_prestacao <= limite_parcela:
    print('Parabéns, seu financiamento foi aprovado! O valor da sua prestação será de R$ {:.2f}.'.format(valor_prestacao))
else:
    print('Infelizmente o valor da prestação R$ {:.2f} é maior que o limite permitido para desconto de R$ {:.2f}.'.format(valor_prestacao, limite_parcela))

