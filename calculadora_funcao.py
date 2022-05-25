from time import sleep


def somar():
    s = a + b
    print (s)
    
def subtrair():
    menos = a - b
    print(menos)
    
def mult():
    multiplicar = a * b
    print(multiplicar)
    
def dividir():
    divisao = a / b
    print(divisao)
    

def lista():
    print('Facilidade','Interpretação','Multiplataforma','Acessibilidade')
    
a = int(input('Digite um número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
opcao = 0
while opcao != 6:

    print('''MENU, ESCOLHA UM NUMERO ABAIXO:
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    [5] - Listar os beneficios do python
    [6] - Sair ''')
    opcao =int(input(">>>>>>Qual sua opção: "))
    if opcao == 1:
        somar()
        
    elif opcao == 2:
        subtrair()
       
    elif opcao == 3:
        mult()
       
    elif opcao == 4:
        dividir()
        
    elif opcao == 5:
        lista()
        
    elif opcao == 6:
        print('Finalizando...')

    else:
        print('Opção invalida, tente um dos outros valores...')  
    print('=-='*10)
    sleep(2)
print('Fim do programa, volte sempre!') 

