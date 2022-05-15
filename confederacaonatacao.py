from datetime import date
atual = date.today().year

print('Confederação Nacional de Natação ')
nome = str(input('Digite seu nome: '))
ano = int(input('Digite o ano de seu NASCIMENTO: '))
idade = atual - ano
print('O atleta tem {} anos!'.format(idade))
if idade <= 9:
    print('Você foi classificado na categoria MIRIM!')
elif 9 < idade <= 14:
    print('Você foi classificado na categoria INFATIL!')
elif 14 < idade <= 19:
    print('Você foi classificado na categoria JUNIOR')
elif 19 < idade < 25:
    print('Você foi classificado na categoria SENIOR!')
else:
    idade >= 25
    print('Você foi classificado na categoria MASTER!')
