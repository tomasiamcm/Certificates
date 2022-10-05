nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print('Seu primeiro nome é {} e o último nome é {}.'.format(separa[0], separa[len(separa)-1]))