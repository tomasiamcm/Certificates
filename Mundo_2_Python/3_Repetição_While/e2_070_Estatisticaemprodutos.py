'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deve perguntar se o usuário vai continuar. Mostrar:
a) total gasto na compra;
b) quantidade de produtos que custam mais de R$ 1.000,00;
c) nome do produto mais barato.
'''

print('=' * 30)
print('LOJA SUPER BARATÃO')
print('=' * 30)

cont = total_compra = cont_valor1000 = valor_barato = 0
nomebarato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total_compra += preco
    if preco > 1000:
        cont_valor1000 += 1
    if cont == 1 or preco < valor_barato:
        valor_barato = preco
        nomebarato = produto
    '''
    if nomebarato == ' ':
        valor_barato += preco
        nomebarato = produto
    else:
        if preco > 1000:
            cont_valor1000 += 1
        if preco < valor_barato:
            valor_barato = preco
            nomebarato = produto   
    '''                     
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
print(f'Você comprou {cont} produtos que totalizou R$ {total_compra:.2f}.')
print(f'Tem {cont_valor1000} produto(s) custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi: {nomebarato}.')
print('=' * 15 + 'FIM DO PROGRAMA' + '=' * 15)

