# Ler um termo e a razão de uma Progressão Aritmética, e mostrar os 10 primeiros termos da PA usando a estrutura while.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite um número inteiro: '))
razao = int(input('Informe qual é a razão da PA: '))
x = int(input('Informe qual o limite da prograssão: '))

termo = primeiro
cont = 1

while cont <= x:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
