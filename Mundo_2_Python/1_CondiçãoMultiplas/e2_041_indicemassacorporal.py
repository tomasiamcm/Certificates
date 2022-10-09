peso = float(input('Informe seu peso: (Kg)'))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

print('Com o peso de {:.1f} Kg e a altura de {:.2f} m o seu IMC é {:.2f}.'.format(peso, altura, imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade morbida.')
