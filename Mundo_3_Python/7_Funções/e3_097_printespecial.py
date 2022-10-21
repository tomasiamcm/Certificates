'''
Faça um programa que tenha uma função escreva(), que recebe um texto qualquer como parâmetro e
mostra uma mensagem com tamanho adaptável.
'''

def escreva(texto):
    print('~' * (len(texto)+4))
    print(f'  {texto}')
    print('~' * (len(texto)+4))


# Programa Principal
texto = str(input('Escreva a frase: '))
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva(texto)

