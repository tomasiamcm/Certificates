'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mpstrado
ou não na o processo de cálculo do fatorial.
'''

def fatorial(n, show=False):
    """_summary_fatorial()
    -> Calcula o Fatorial de um número.

    Args:
        n (_type_): _número que será usado para cálculo do fatorial_
        show (bool, optional): _informa se o cálculo deve ser ou não mostrado_. Defaults to False.

    Returns:
        _type_: _retorna o valor do Fatorial de um número n_
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
n = int(input('Informe o número para o cálculo fatorial: '))
print(fatorial(n, show=True))
#help(fatorial)
