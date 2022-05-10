import random
a= str(input('Digite o Nome do primeiro aluno: '))
b = str(input('Digite o Nome do segundo aluno: '))
c = str(input('Digite o Nome do terceiro aluno: '))
d = str(input('Digite o Nome do quarto aluno: '))
lista = [a, b, c, d]
escolhido = random.choice(lista)

print('O aluno escolhido foi  {}'.format(escolhido))