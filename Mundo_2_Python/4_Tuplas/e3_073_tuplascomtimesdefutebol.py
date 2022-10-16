'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocação.
Mostre:
a) os primeiros 5 colocados;
b) os últimos 4 colocados;
c) os times em ordem alfabética;
d) em que posição está o time da chapecoense.
'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético PR', 'São Paulo', 'Internacional',
        'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético MG', 'Fluminense',
        'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('-=' * 20)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição.')