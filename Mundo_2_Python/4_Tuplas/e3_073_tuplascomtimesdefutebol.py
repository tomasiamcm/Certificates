'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocação.
Mostre:
a) os primeiros 5 colocados;
b) os últimos 4 colocados;
c) os times em ordem alfabética;
d) em que posição está o time da chapecoense.
'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético PR', 'São Paulo', 'Internacional',
        'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético MG', 'Fluminense', 'Botafogo',
        'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')


print(times[0:4])
print(times[17:21])
print(sorted(times))
print(slice(times('Chapecoense')))