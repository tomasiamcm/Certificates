# Tabuada

n = int(input('Informe qual o número que deseja para a tabuada: '))

for t in range(1, 11):
    print('{} x {} = {}'.format(n, t, n * t))