# from math import sqrt, pow

# ceil => arredonda pra cima
# floor => arredonda pra baixo
# trunc => truncar número
# pow => calcula potencia
# sqrt => calcula raiz quadrada
# factorial => calcula fatorial

#####################     IMPORTANDO MODULO: MATH       #######################
'''
import math

num = int(input('Informe um número: '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} é {:.2f}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é {:.2f}'.format(num, math.floor(raiz)))
'''


#####################     IMPORTANDO MODULO: RANDOM       #######################
'''
import random
num = random.random()    => PADRAO ENTRE 0 E 1
num1 = random.randint(1, 10)

print(num)
print(num1)
'''

#####################     IMPORTANDO BIBLIOTECA: EMOJI       #######################

import emoji

print(emoji.emojize("Olá, mundo :earth_americas:", use_aliases=True))


