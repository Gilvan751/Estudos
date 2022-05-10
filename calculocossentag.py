import math
num = float(input('Digite um ângulo qualquer :  '))
x = math.cos(math.radians(num))
y = math.sin(math.radians(num))
z = math.tan(math.radians(num))
print('O ângulo de  {} º tem como \n coseno {:.2f}, \n seno {:.2f} e \n tangente {:.2f}'.format(num, x, y, z))