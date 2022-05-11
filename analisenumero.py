num = int(input('Informe um numero...'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número...{}'.format(num))
print('Milhar: {}'.format(m))
print('Centena:  {}'.format(c))
print('Dezena:  {}'.format(d))
print('Unidade:  {}'.format(u))