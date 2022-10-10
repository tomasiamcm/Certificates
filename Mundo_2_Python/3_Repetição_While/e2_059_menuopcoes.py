num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º núumero: '))

menu = 0

while menu != 5:
    print('-=' * 20)
    print('''Escolha uma das opções abaixo:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    menu = int(input('Qual a opção desejada? '))

    if menu == 1:
        resultado = num1 + num2
        print('A soma de {} e {} é {}.'.format(num1, num2, resultado))
        print('-=' * 20)
    elif menu == 2:
        resultado = num1 * num2
        print('A multiplicação de {} e {} é {}.'.format(num1, num2, resultado))
        print('-=' * 20)
    elif menu == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número entre {} e {} é {}.'.format(num1, num2, maior))
        print('-=' * 20)
    elif menu == 4:
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º núumero: '))

print('FIM')
