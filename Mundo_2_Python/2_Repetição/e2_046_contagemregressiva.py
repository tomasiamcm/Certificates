# Realizar a contagem regressiva de 10 a 0, com um espaço de tempo de 1s entre a contagem.
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Boom')