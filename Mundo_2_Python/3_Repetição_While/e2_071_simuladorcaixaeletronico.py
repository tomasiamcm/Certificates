'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
Pergunte ao cliente: 
a) qual o valor do saque;
b) informar quantas cédulas de cada valor seão entregues.;
Considere que o caixa possui cédulas de R$ 50,00, R$ 20, R$ 10,00 e R$ 1,00.
'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

saldo = valor_saque = int(input('Qual valor deseja sacar? '))
valor_cedula = 50
cont_cedulas = 0

while True:
    if saldo >= valor_cedula:
        saldo -= valor_cedula
        cont_cedulas += 1
    else:
        if cont_cedulas > 0:
            print(f'Total de {cont_cedulas} cédulas de R$ {valor_cedula:.2f}.')
        if valor_cedula == 50:
            valor_cedula = 20
        elif valor_cedula == 20:
            valor_cedula = 10
        elif valor_cedula == 10:
            valor_cedula = 1
        cont_cedulas = 0
        if saldo == 0:
            break

############################ Outra forma ################################
'''
cont_50 = cont_20 = cont_10 = cont_1 = 0

while True:
    if saldo >= 50:
        saldo -= 50
        cont_50 += 1
    elif saldo >= 20:
        saldo -= 20
        cont_20 += 1
    elif saldo >= 10:
        saldo -= 10
        cont_10 +=1
    else:
        saldo -= 1
        cont_1 += 1
    if saldo == 0:
        break
print(f'Para sacar o valor desejado foi necessário: {cont_50} de R$ 50,00, {cont_20} de R$ 20,00, {cont_10} de R$ 10,00 e {cont_1} de R$ 1,00.')
'''

print('=' * 30)
print('Volte sempre ao Banco CEV! TEnha um bom dia!')
