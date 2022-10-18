'''
Crie um programa para receber 7 números e coloque-os em uma lista, sendo:
a) números pares;
b) números impares.
'''
'''
lista = []
pares = []
impares = []

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(pares[:])
lista.append(impares[:])
pares.clear()
impares.clear()
print(lista)
print(f'Os números pares são: lista[0]')
print(f'Os números ímpares são: lista[1])

'''
############################ Outra forma ######################

lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Informe o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print('-=' * 30)
lista[0].sort()
print(f'Os números pares são: {lista[0]}')
lista[1].sort()
print(f'Os números ímpares são: {lista[1]}')
