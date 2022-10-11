# Ler um termo e a razão de uma Progressão Aritmética, e mostrar os 10 primeiros termos da PA usando a estrutura while.
# Após deve perguntar ao usuário quantos termos a mais ele quer ver, até que ele não queira mais termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite um número inteiro: '))
razao = int(input('Informe qual é a razão da PA: '))
termo = primeiro
cont = 1
x = 10
y = 0

while x != 0:
    y = y + x
    while cont <= y:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    x = int(input('Informe quantos termos você quer mostrar a mais: '))
print('FIM" Progressão finalizada com {} termos mostrados.'.format(y))
