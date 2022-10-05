import calendar
import datetime
#from calendar import isleap

ano = int(input('Informe o ano (coloque 0 para ano atual): '))

if ano == 0:
    ano = datetime.date.today().year

if calendar.isleap(ano):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))


#######################     Outra Forma       ######################
'''
ano = int(input('Ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano informado é bissexto.')
else:
    print('O ano informado não é bissexto.')
'''