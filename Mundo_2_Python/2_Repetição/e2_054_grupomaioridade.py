# Verificar se uma pessoa pertence ao grupo da maioridade. Considera-se 21 anos para maioridade.

from datetime import date

maioridade = 21
ano_atual = date.today().year
total_maior = 0
total_menor = 0

for n in range(1, 8):
    ano_nasc = int(input('Informe o ano que a {}ª pessoa nasceu: '.format(n)))
    idade = ano_atual - ano_nasc
    if idade >= maioridade:
        total_maior += 1
    else:
        total_menor += 1
        
print('Ao todo tivemos {} pessoas maiores de idade e {} menores de idade.'.format(total_maior, total_menor))
