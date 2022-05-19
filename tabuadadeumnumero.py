from time import sleep
numero = int(input('DIGITE um número para sua tabuada: '))
print('Tabuada do numero {}'. format(numero))
for c in range(1, 11):
    sleep(1)
    print('\t', '{} x {:2} = {}'.format(numero, c, numero * c))
print(
    f'\t Parabéns, agora você pode estudar a tabuada do {numero} com mais facilidade!')
