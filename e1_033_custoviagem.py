distancia = float(input('Informe a distância da viagem em Km: '))
valor_viagem = 0

if distancia <= 200:
    valor_viagem = (distancia * 0.50)
else:
    valor_viagem = (distancia * 0.45)

print('O valor da sua viagem de {} km custará R$ {:.2f}.'.format(distancia, valor_viagem))



