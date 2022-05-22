from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasceu = int(input('Em que ano a {}º pessoa nasceu: '.format(pess)))
    idade = atual - nasceu
    if idade >= 21:
        totalmaior += 1

    else:
       totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totalmenor))
