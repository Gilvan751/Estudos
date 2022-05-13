casa = float(input('Qual o valor da casa que você deseja financiar?R$   '))
salario = float(input('Quanto você ganha por mês?R$ '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = casa / (12 * anos)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos '.format(
    casa, anos), end='')
#print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos ', end='')
print(' a prestação da casa será de R$ {:.2f}'.format(prestacao))
#print(f' a prestação da casa será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
