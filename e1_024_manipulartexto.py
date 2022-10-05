nome_completo = str(input('Digite seu nome completo: ')).strip()

# Nome em letra maiuscula
print('Seu nome em letra maiúscula é: {}'.format(nome_completo.upper()))

# Nome em letra minuscula
print('Seu nome em letra minúscula é: {}'.format(nome_completo.lower()))

# Quantas letras tem SEM espaço
print('Seu nome tem ao todo {} letras sem contar os espaços.'.format(len(nome_completo) - nome_completo.count(' ')))

# Quantas letras tem COM espaço
print('Seu nome tem ao todo {} letras contando os espaços.'.format(len(nome_completo)))

# Quantas letas tem o 1º nome
print('Seu 1º nome tem {} letras.'.format(nome_completo.find(' ')))

# Outra forma de fazer
separa = nome_completo.split()
print('Seu 1º nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))