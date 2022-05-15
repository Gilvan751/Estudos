'''Calcula da existência de um triangulo dado os lados'''
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um tringulo',  end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')

else:
    print('Os segmento acima não podem formar um triangulo')
