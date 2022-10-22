'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
a) Quantidade de notas
b) A maior nota
c) A menor nota
d) A média da turma
e) A situação (opcional)
Adicione também as docstrings da função.
'''

def notas(*nota, situacao=False):
    """_summary_Função para análise de notas dos alunos

    Args:
        situacao (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: Retorna a soma, máxima, mínima, média das notas e a situação do aluno.
    """
    r = dict()
    r['total'] = len(nota)
    r['max'] = max(nota)
    r['min'] = min(nota)
    r['media'] = sum(nota) / len(nota)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resultado = notas(9, 10, 5.5, 2.5, 1.5, situacao=True)
print(resultado)
help(notas)
