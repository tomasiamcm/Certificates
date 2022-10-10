from random import randint

print('Sou seu computador... Acabei de pensar num número entre 0 e 10. Será que você consegue advinhar? ')
jogador = int(input('Qual o seu palpite? '))

computador = randint(0, 10)

palpites = 1


while jogador != computador:
    jogador = int(input('Você não acertou. Tente novamente! Informe um número entre 0 e 10: '))
    palpites += 1

print('Parabéns! Você acertou com {} tentativas.'.format(palpites))