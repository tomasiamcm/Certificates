velocidade = float(input('Informe a velocidade do carro: '))
limite = 80
multa_km = 7
valor_multa = 0


if velocidade > limite:
    print('MULTADO! Você ultrapassou o limite permitido de {} km/h.'.format(limite))
    valor_multa = (velocidade - limite) * multa_km
    print('O Valor da multa é: R$ {:.2f}'.format(valor_multa))
else:
    print('Parabéns! Você está dirigindo dentro da velocidade permitida.')


