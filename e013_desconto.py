preco = float(input('Informe o preço do produto: '))
desconto = 5

valor_pagar = preco - (preco * (desconto/100))

print('O produto custava R$ {:.2f}, na promoção com {:.0f}% de desconto, fica no valor de R$ {:.2f}.'.format(preco, desconto, valor_pagar))