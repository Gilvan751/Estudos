''' n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1


if (n == 1) or (n == 2):
    print("1")
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo) '''
print('-'*20) 
print("""Sequência de Fibonacci """)
print('-'*20)
n = int(input("Quantos termos você quer mostrar na Sequencia de Fibonacci: "))
t1 = 0
t2 = 1

print('~'*62)
print('{} => {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('=> {} '.format(t3), end="")
    t1 = t2
    t2 = t3
    cont +=1
print(' -> FIM')
print('~'*62,"\n")
    



''' if (n == 1) or (n == 2):
    print("1")
else:
    for count in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo) '''

