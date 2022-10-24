def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if not formato else moeda(resultado)


def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if not formato else moeda(resultado)


def dobro(preco=0, formato=False):
    resultado = preco * 2
    return resultado if not formato else moeda(resultado)


def metade(preco=0, formato=False):
    resultado = preco / 2
    return resultado if not formato else moeda(resultado)


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxad=13):
    print('-' * 35)
    print('RESUMO DO PREÇO'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco):>10}')
    print(f'Metade do preço: \t{metade(preco, True):>10}')
    print(f'Dobro do preço: \t{dobro(preco, True):>10}')
    print(f'Acréscimo de \t{taxaa}%: {aumentar(preco, taxaa, True):>13}')
    print(f'Decréscimo de 13% é de \t{diminuir(preco, taxad, True):>10}')
    print('-' * 35)

