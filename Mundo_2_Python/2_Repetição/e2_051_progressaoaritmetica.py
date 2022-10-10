# Ler um termo e a razão de uma Progressão Aritmética, e mostrar os 10 primeiros termos da PA.

primeiro = int(input('Digite um número inteiro: '))
razao = int(input('Informe qual é a razão da PA: '))
decimo = primeiro + (10 - 1) * razao

for n in range(primeiro, decimo + razao, razao):
    print('{}'.format(n), end=' -> ')
print('FIM')