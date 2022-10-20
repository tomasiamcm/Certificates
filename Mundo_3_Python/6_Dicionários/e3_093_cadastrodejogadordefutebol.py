'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador, quantas partidas ele jogou e quantos gols feito em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

dados = {}
gols_partida = []
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, dados['partidas']):
    gols_partida.append(int(input(f'Quantos gols na partida {c+1}?')))
    dados['total_gols'] = sum(gols_partida)
dados['gols'] = gols_partida[:]

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
print()
for i, v in enumerate(dados):
    print(f'=> Na partida {i+1} ele fez {dados["gols"]} gols.')
print(f'Foi um total de {dados["total_gols"]} gols.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} fez {dados["total_gols"]} gols em {dados["partidas"]} partidas.')
