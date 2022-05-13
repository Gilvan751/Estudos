#from calendar import isleap
#ano = int(input('Digite o ano atual para saber se é bissexto '))
#if isleap(ano):
  #  print('É bissexto')
#else:
 #   print('Não é bissexto')
from datetime import date
ano = int(input('Digite o ano que você quer saber se é bissexto  '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))