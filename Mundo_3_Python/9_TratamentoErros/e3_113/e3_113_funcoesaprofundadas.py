'''
Reescreva a função leiaInt() que fizemos no desafio i04, cinlcuindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a
mesma funcionalidade.
'''
from funcoes import funcao

# Programa principal
nInt = funcao.leiaInt('Digite um número inteiro: ')
nReal = funcao.leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {nInt} e o real foi {nReal}.')
