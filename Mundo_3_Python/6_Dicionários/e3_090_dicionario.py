'''
Faça um programa que leia nome e média de um aluno e guarde em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

boletim = {}

boletim['nome'] = str(input("Nome: "))
boletim['media'] = float(input("Média: "))
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
elif boletim['media'] >= 5:
    boletim['situacao'] = 'Em recuperação'
else:
    boletim['situacao'] = 'Reprovado'
continua = ' '

print('-=' * 30)
print(f'{boletim["nome"]} teve a média {boletim["media"]} e a situação é: {boletim["situacao"]}.')
print('-=' * 30)

################### Outra forma ##################
'''
for k,v in boletim.items():
    print(f'{k} é {v}')
'''
