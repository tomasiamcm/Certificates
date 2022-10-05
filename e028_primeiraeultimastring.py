frase = str(input('Digite uma frase: ')).upper().strip()

# Verificando quantas vezes a letra A aparece na frase
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print(frase.count('A'))

# Verificando quando aparece a letra A pela 1ª vez
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))

# Verificando quando aparece a letra A pela última vez
print('A primeira letra "A" aparece na posição {}'.format(frase.rfind('A')+1))
