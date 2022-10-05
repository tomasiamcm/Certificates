largura = float(input('Informa a largura da parede: '))         # medida: metros
altura = float(input('Informe a altura da parede: '))           # medida: metros
tinta = 2                                             # medida: 1 litro para 2 metros quadrados


area_parede = largura * altura

quantidade_tinta = area_parede / tinta

print('São necessários {} litros de tinta para pintura da parede com {} m².'.format(quantidade_tinta, area_parede))