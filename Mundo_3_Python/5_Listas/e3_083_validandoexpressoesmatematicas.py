'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta.
'''
'''
expressao = str(input('Digite a expressão deseja: '))

cont_a = 0
cont_f = 0

for i in expressao:
    if i == '(':
        cont_a += 1
    if i == ')':
        cont_f += 1

if cont_a == cont_f:
    print('SUa expressão é válida.')
else:
    print('Sua expressão não é válida.')
'''

############################ Outra forma ###############################

expressao = str(input('Digite a expressão deseja: '))
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')
