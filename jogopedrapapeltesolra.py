from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('Jogador VENCE')

    elif jogador == 2:
        print('Computador VENCE')

    else:
        print('\033[1;31m Jogada INVÁLIDA')
elif computador == 1:  # Computador jogou PAPEL

    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('\033[1;31m Jogada INVÁLIDA')

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[1;31m Jogada INVÁLIDA')
else:

    print('\033[1;31m Jogada INVÁLIDA')
