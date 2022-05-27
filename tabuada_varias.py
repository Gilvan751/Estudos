from time import sleep
while True:
    num = int(input('Quer ver a tabuada de qual numero: '))
    if num < 0:
        break
    print('-=-'*30)
    for c in range(1, 11):
        sleep(1)
        print(f"\t {num} x {c:2} = {num * c}")
    print('-=-'*30)
print('Programa TABUADA encerrada. Volte Sempre!\n ')

