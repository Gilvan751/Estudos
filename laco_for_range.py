from time import sleep
print('Entrando no laço...')
for i in range(10):
    print(i)
    sleep(.8)
    if(i == 8):

        break
sleep(.8)
print('Saindo do loop....')
