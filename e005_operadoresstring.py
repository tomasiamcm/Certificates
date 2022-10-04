# OPERADORES COM STRING

# Concatenar
# print('Oi' + 'Olá')

# Replicando informações
nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {}!'.format(nome)) # Prazer em te conhecer Tomásia!
print('Prazer em te conhecer {:20}!'.format(nome)) # Escreve o nome em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) # Escreve o nome alinhado à direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # Escreve o nome alianhado à esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # Escreve o nome centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) # Escreve o nome centralizado com sinais de igual em volta
