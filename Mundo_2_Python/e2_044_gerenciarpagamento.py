print('{:=^40}'.format(' LOJAS GUANABARA '))

preco = float(input('Qual o valor das compras: R$ '))
print('''Escolha a forma de pagamento desejada: 
[1] A vista: Dinheiro/Cheque
[2] A vista: cartao
[3] 2x no cartao
[4] 3x ou mais no cartão
''')

pagamento = int(input('Qual a opção escolhida para pagamento? '))

if pagamento == 1: # Pagamento à vista com dinheiro ou cheque
    desconto = 10
    valor_final = preco - (preco * (desconto / 100))
    print('Sua compra de R$ {:.2f} terá {}% de desconto e custará R$ {:.2f} para pagamento à vista em dinheiro ou cheque.'.format(preco, desconto, valor_final))
elif pagamento == 2: # Pagamento à vista com cartão
    desconto = 5
    valor_final = preco - (preco * (desconto / 100))
    print('Sua compra de R$ {:.2f} terá {}% de desconto e custará R${:.2f} para pagamento à vista no cartão.'.format(preco, desconto, valor_final))
elif pagamento == 3: # Pagamento em até 2x com cartão
    parcelas = 2
    valor_parcela = preco / parcelas
    print('Sua compra de R$ {:.2f} pode ser pago no cartão em 2x de {:.2f} sem juros.'.format(preco, valor_parcela))
elif pagamento == 4: # Pagamento a partir de 3x com cartão
    parcelas = int(input('Informe a quantidade de parcelas: '))   
    if parcelas < 3:
        print('Esta opção de pagamento é válida para 3 ou mais parcelas. Tente novamente!')
    else:
        juros = 20
        valor_final = preco + (preco * (juros /100))
        valor_parcela = valor_final / parcelas
        print('Sua compra de R$ {:.2f} poderá ser paga em {}x de R$ {:.2f} com juros de {}%, totalizando R$ {:.2f}.'.format(preco, parcelas, valor_parcela, juros, valor_final))
else:
    print('Opção inválida de pagamento. Tente novamente!')