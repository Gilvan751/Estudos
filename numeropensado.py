from random import randint
computador = randint(0, 5)  # faz o computador pensar
print('-='*30)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-='*30)
jogador = int(input('Em que numero eu pensei '))
print('Pensei no numero {}'.format(computador))
if jogador == computador:
    print('Parabéns! você conseguiu me vencer!')    
else:
    print('Ganhei! eu pensei no numero {} e não no numero {}'.format(
        computador, jogador))
