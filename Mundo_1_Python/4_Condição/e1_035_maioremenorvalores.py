a = int(input('Informe o 1º número: '))
b = int(input('Informe o 2º número: '))
c = int(input('Informe o 3º número: '))

min = a

if b < a and b < c:
    min = b
else:
    min = c

max = a

if b > a and b > c:
    max = b
if c > a and c > b:
    max = c


#print('{}, {}, {}'.format(num1, num2, num3)
print(min)
print(max)