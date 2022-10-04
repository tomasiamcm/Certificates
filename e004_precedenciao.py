''' PRECEDÊNCIA OPERAÇÕES MATEMÁTICAS
** => potência
* => multiplicação
/ => divisão
// => divisão inteiro
% => resto
+ => soma
- => subtração
'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Soma
soma = num1 + num2

# Subtração
subtracao = num1 - num2

# Multiplicação
multiplicacao = num1 * num2

# Divisão
divisao = num1 / num2

# Divisão (valor inteiro)
divisao_inteira = num1 // num2

# Resto da divisão
resto = num1 % num2

# Potenciação
potenciacao = num1 ** num2

print('A soma de {} e {} é: {}'.format(num1, num2, soma))
print('A subtração de {} e {} é {}'.format(num1, num2, subtracao))
print('A multiplicação de {} e {} é: {}'.format(num1, num2, multiplicacao))
print('A divisão de {} e {} é {}'.format(num1, num2, divisao))
print('A divisão inteira de {} e {} é {}'.format(num1, num2, divisao_inteira))
print('O resto da divisão de {} e {} é {}'.format(num1, num2, resto))
print('O resulta da potenciação de {} e {} é {}'.format(num1, num2, potenciacao))