'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador, quantas partidas ele jogou e quantos gols feito em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

dados = {}
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

dados['total_gols'] = 0

for c in dados['partidas']:
    dados['gols'] = int(input(f'Quantos gols na partida {c}?'))
    dados['total_gols'] += dados['gols']

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados:
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]}.', end='')
for i, v in enumerate(dados):
    print(f'=> Na partida {i+1} ele fez {dados["gols"]} gols.')
print(f'Foi um total de {dados["total_gols"]}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} fez {dados["total_gols"]} gols em {dados["partidas"]} partidas.')
