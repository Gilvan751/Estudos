num = int(input('\033[1;34m Digite qualquer numero inteiro:  '))
resto = num % 2
if resto == 0:
    print(' O número {} é  \033[1;32m  PAR'.format(num))
else:
    print('O número {} é   \033[1;31m  ÍMPAR'.format(num))
