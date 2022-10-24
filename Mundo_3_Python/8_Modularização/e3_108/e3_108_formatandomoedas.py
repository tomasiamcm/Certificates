'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
os números como um valor monetário formatado.
'''
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O valor de {moeda.moeda(p)} acrescido de 10% é de {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'O valor de {moeda.moeda(p)} reduzido de 13% é de {moeda.moeda(moeda.diminuir(p, 13))}')

