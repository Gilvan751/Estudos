'''Pega os valores pares e soma do conjuto de 6 valores atribuidos pelo aluno'''
soma = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {}º valor:'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} numeros PARES e a soma foi {}'.format(cont, soma))
