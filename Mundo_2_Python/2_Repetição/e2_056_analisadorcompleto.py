''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    Informe a média de idade, o nome da pessoa mais velha e quantas mulheres tem menos de 20 anos.'''

somaidade = 0
media = 0
idade_mais_velho = 0
homem_mais_velho = ''
cont_mulheres_20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Informe o nome: ')).strip().upper()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: [F/M]: ')).strip().upper()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        cont_mulheres_20 += 1
    if sexo == 'M' and idade > idade_mais_velho:
        idade_mais_velho = idade
        homem_mais_velho = nome

media = somaidade / p

print('A média de idade do grupo é de {} anos.'.format(media))
print('O Homem mais velho é {} e tem {} anos.'.format(homem_mais_velho, idade_mais_velho))
print('No grupo tem {} mulher(es) com menos de 20 anos.'.format(cont_mulheres_20))
