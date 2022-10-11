'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos;
b) quantos homens foram cadastrados;
c) quantas mulheres tem menos de 20 anos.
'''
print('=' * 15 + ' CADASTRE UMA PESSOA ' + '=' * 15)

cont_18anos = cont_mulher = cont_homem = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    if idade > 18:
        cont_18anos += 1
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0] 
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break        
print(f'Total de pessoas com mais de 18 anos: {cont_18anos}, total de homens: {cont_homem} e total de mulheres com menos de 20 anos: {cont_mulher}.')
