from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'Numeros sorteados {n} ')
print(f'\nO maior valor sorteado foi : {max(numeros)}')
print(f'\nO menor valor sorteado foi : {min(numeros)}')