'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guarde-os em um dicionário e todos os
dicionários em uma lista.
No final, mostre:
a) quantas pessoas foram cadastradas;
b) a média de idade do grupo;
c) uma lista com todas as mulheres;
d) uma lista com todas as pessoas com idade acida da média.
'''

lista = []
pessoas = {}
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
        if pessoas['sexo'] in 'FM':
            break
        else:
            print('ERRO! Digite apenas F ou M.')
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    media = soma / len(lista)
    while True:
        continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continua == 'N':
        break
    
print(lista)
print(pessoas)
print('-=' * 30)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='') 
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<<< ENCERRADO >>>')