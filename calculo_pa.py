print('-='*15)
print('Escreva uma PA de 10 termos')
print('-='*15)
a = int(input('Digite o primeiro termo da PA: '))
r = int(input(('Digite a razão da PA: ')))
d = a + 10 * r
for p in range(a, d, r):
    print('{}'.format(p), end=' => ')
print('ACABOU!!!!!')
