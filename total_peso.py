totalmaior = 0
totalmenor = 0
for p in range(1, 6):
    peso = float(input('Qual é peso {}º da pessoa: '.format(p)))
    if p == 1:
        totalmaior = peso
        totalmenor = peso
    else:
        if peso > totalmaior:
            totalmaior = peso
        if peso < totalmenor:
            totalmenor = peso
print('O maior peso lido foi de {} Kg'.format(totalmaior))
print('O menor peso lido foi de {} Kg'.format(totalmenor))
