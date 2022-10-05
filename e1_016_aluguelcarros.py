dias = int(input('Informe a quantidade de dias de uso do veículo: '))
km = float(input('Informe q quantidade de Km percorrido: '))

valor_diaria = 60.00
valor_Km = 0.15

valor = (km * valor_Km) + (dias * valor_diaria)

print('O valor do aluguel do carro por {} dias e {} km rodado é de R$ {:.2f}.'.format(dias, km, valor))


