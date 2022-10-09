num = int(input('Informe um número: '))

print('''Escolha uma das opções abaixo:
[1] Converte para Binário
[2] Converte para Octal
[3] Converte para Hexadecimal
''')

opcao = int(input('Digite a opção escolhida: '))

if opcao == 1:
    print('O {} convertido para Binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O {} convertido para Octal é {}.'.format(num, oct(num)[2:]))
else:
    print('O {} convertido para Hexadecimal [e {}.'.format(num, hex(num)[2:]))