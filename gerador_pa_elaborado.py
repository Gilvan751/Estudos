print("Gerador de PA")
print("=-="*10)
a = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
t = a
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais 
    while cont <= total:
        print('{} => '.format(t), end='')
        t += r
        cont += 1

    print('Pauda....\n')
    mais = int(input("Digite 0 para terminar ou a quantidade de termos que você quer mostrar mais: "))
print("Terminou a execussão.....")
