'''Conversão de Números'''
num = int(input('Digite um numero inteiro : '))
print("""Escolha uma das conversões: 
      [1] converter o numero para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL """)
opcao = int(input('Sua opção : '))
if opcao == 1:
    print('{} convertido em BINÁRIO é igual a \033[1;34m{} '.format(
        num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL  é igual a \033[1;33m{} '.format(
        num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é igual a \033[1;32m{}'.format(
        num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente!')
