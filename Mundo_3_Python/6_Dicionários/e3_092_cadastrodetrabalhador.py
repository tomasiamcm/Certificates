'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade),
se por acaso a CTPS for diferente de zero , o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Considere: 35 anos de colaboração
'''
from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
#print(dados)
print(f'{dados["nome"]} tem {dados["idade"]} anos e o número da CTPS é: {dados["ctps"]}. O ano de contratação foi {dados["ano_contratacao"]}, salário R$ {dados["salario"]} e se aposentará com {dados["aposentadoria"]} anos.')

################### Outra forma ##################
'''
for k,v in boletim.items():
    print(f' - {k} tem o valor {v}')
'''