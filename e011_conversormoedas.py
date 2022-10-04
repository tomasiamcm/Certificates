valor = float(input('Informe o valor que você tem na carteira: R$ '))
cambio_dolar = 3.27

valor_convertido = valor / cambio_dolar

print('Com o valor de R$ {:.2f} você pode comprar $ {:.2f} dolares.'.format(valor, valor_convertido))
