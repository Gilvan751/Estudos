from datetime import date

num = int(input('Digite o ano de seu nascimento: '))
year = date.today().year
data_atual = year - num
dez = num + 18
res = year - dez

print('Atualmente você tem {} anos '.format(data_atual))
if data_atual > 18:
    print('Você completou 18 anos no ano de {} ja se passaram {} anos '.format(dez, res))
elif data_atual < 18:
    print('Você completará 18 anos  no ano de {} é faltam {} anos para você se ALISTAR!'.format(
        dez, dez - year))
elif data_atual == 18:
    print('Você esta no ano de seu ALISTAMENTO!'.format(data_atual))
