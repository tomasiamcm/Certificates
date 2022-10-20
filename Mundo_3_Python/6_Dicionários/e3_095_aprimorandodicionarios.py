'''
Pegue o desafio 093 para que leia vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
'''

time = []
dados = {}
gols_partida = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols_partida.clear()
    for c in range(0, dados['partidas']):
        gols_partida.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['gols'] = gols_partida[:]
    dados['total_gols'] = sum(gols_partida)
    time.append(dados.copy())
    while True:
        continua = str(input('Deseja cadastrar mais um jogador? [S/N]')).upper().strip()[0]
        if continua in 'SN':
            break
        else:
            print('ERRO! Digite S ou N.')
    if continua == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para encerrar) '))
    if jogador == 999:
        break
    elif jogador < 0 or jogador >= len(time):
        print(f'ERRO! Não existe jogador com o código {jogador}. Tente novamente!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR: {time[jogador]["nome"]}')
        for i, g in enumerate(time[jogador]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')
