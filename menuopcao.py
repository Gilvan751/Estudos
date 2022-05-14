from time import sleep
print('\tMenu de opção para efetuar\n\toperação entre dois números')
n1 = float(input('Digite o primeiro numero '))
n2 = float(input('Digite o segundo  numero '))
opcao = 0
while opcao != 5: 
    print(''' Menu de opção
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Digitar outro numero
          [5] Sair do programa''')
    opcao = int(input('Qual sua opção? '))
    if opcao ==1:
        soma = n1 + n2
        print(f'O valor da soma entre {n1:.1f} + {n2:.1f} = {soma} ')
    elif opcao ==2:
        mult = n1 * n2
        print(f'O valor da Multiplicação  entre {n1:.1f} * {n2:.1f} = {mult} ')
    elif opcao ==3:
        if n1 > n2:
            print(f'O maior número entre {n1:.1f} e {n2:.1f} é {n1:.1f}')
        elif n1 == n2:
            print(f'Os dois números {n1:.1f} e {n2:.1f} são iguais {n1:.1f}')
        else:
            print(f'O maior número entre {n1:.1f} e {n2:.1f} é {n2:.1f}')
    elif opcao == 4:
        print('Digite os dois números: ')
        n1 = float(input('Digite o primeiro numero '))
        n2 = float(input('Digite o segundo  numero '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Digite um valor valido ')
    print('=-='*10)
    sleep(2)
print('Fim do Programa. Volte Sempre!')