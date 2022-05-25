print("Gerador de PA")
print("=-="*10)
a = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
t = a
cont = 1
while cont <= 10:
    print('{} => '.format(t),end='')
    t += r
    cont+=1
  
print('Fim....\n')
