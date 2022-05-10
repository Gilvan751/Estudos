s = float(input('Digite o valor do salário do funcionário: R$ '))
r = (s * 0.15)  + s
print('O salário que era R$ {:.2f} com o aumento de 15% passou a ser de R$ {:.2f}'.format(s, r))