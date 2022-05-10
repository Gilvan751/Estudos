from math import hypot
x = float(input('Digite um valor para o cateto oposto: '))
y = float(input('Digite um valor para o cateto adjacente:  '))
'''z = (x**2 + y**2)**(1/2)
print('A hipotenusa desse triangulo é {:.2f}'.format(z))'''
z = hypot(x,y)
print('O valor da hipotenusa desse triangulo é {:.1f}'.format(z))