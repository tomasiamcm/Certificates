import math

angulo = int(input('Informe o valor do ângulo: '))

seno = math.sin(math.radians(angulo))       # cateto_oposto / hipotenusa
cosseno = math.cos(math.radians(angulo))    # cateto_adjacente / hipotenusa
tangente = math.tan(math.radians(angulo))   # cateto_oposto / cateto_adjacente

print('O angulo de {:.2f} tem o Seno de {:.2f}, o Cosseno de {:.2f} e a Tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))

