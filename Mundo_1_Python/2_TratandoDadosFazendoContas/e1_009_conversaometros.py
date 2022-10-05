# Km hm dam m dm cm mm
medida = int(input('Digite a quantidade de metros que deseja converter: '))
km = medida / 1000                     # Convertendo para quilometros
hm = medida / 100                      # Convertendo para hectômetros
dam = medida / 10                      # Convertendo para decâmetros
dm = medida * 10                       # Convertendo para decímetros
cm = medida * 100                      # Convertendo para centímetros
mm = medida * 1000                     # Convertendo para milímetros


print('{} metros equivalem a {} quilometros.'.format(medida, km))
print('{} metros equivalem a {} hectômetros.'.format(medida, hm))
print('{} metros equivalem a {} decâmetros.'.format(medida, dam))
print('{} metros equivalem a {} decímetros.'.format(medida, dm))
print('{} metros equivalem a {} centrímetros.'.format(medida, cm))
print('{} metros equivalem a {} milímetros.'.format(medida, mm))
