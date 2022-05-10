x = float(input('Digite o comprimento da parede: '))
y = float(input('Digite o valor da largura da parede: '))
a = x * y
t = a / 2
g = t/18

l = t*3.6
print('Sua parede tem as dimensões de {:.2f} m x {:.2f} m e sua area é de {:.2f} m²'.format(x, y, a))
print('A area da parede é de {:.2f} m², e vai gastar de tinta a quantia de {:.2f} litros de tinta, e se comprar em galão de 18l vai gastar {:.1f} latas'.format(a, t, g))
print('Se você for comprar lata de 3.6 litros gastará  {:.2f} litros'.format(l))