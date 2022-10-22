'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o 
ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
Negado, Opcional ou Obrigatório nas eleições.
'''

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

