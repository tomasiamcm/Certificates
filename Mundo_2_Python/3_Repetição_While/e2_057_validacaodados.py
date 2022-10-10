# Faça um programa que leio o sexo de uma pessoas, mas só pode aceitas os valor M ou F.

sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
# idade = int(input(''))
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Informe o sexo [F/M]: ')).strip().upper()[0]
    print('Só são aceitas as opções: F ou M. Tente novamente!')
    
print('VOcê digitou o sexo {}.'.format(sexo))
 