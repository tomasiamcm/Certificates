import math

'''
cateto_oposto = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente = float(input('Informe o valor do cateto adjacente: '))

hipotenusa = math.sqrt((math.pow(cateto_oposto, 2)) + (math.pow(cateto_adjacente, 2)))

# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
'''

cateto_oposto = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente = float(input('Informe o valor do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))