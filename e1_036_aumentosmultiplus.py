salario = float(input('Qual o seu salário: '))

faixa_salario = 1250
reajuste1 = 15
reajuste2 = 10

if salario <= faixa_salario:
    salario_novo = salario + (salario * reajuste1 / 100)
    print('Seu salário de R$ {:.2f} será reajustado em {}% passando para R$ {:.2f}.'.format(salario, reajuste1, salario_novo))
else:
    salario_novo = salario + (salario * reajuste2 / 100)
    print('Seu salário de R$ {:.2f} será reajustado em {}% passando para R$ {:.2f}.'.format(salario, reajuste2, salario_novo))

