#tamanho propriedades
l = 'lista de letras'
data = '24/05/2022'

tamanho = len(l)
print(tamanho)
#split da string serve para dividir intervalos que vão utilizar
lista = l.split(" ")
lista2 = data.split('/')
print(lista)
print(lista2)
#substituição substituir um espaço ou qualquer palavra por outra replace
print(l.replace("de",""))
#fatiamento e divisão de string[0] [1:3] [1:2:4]
nome = 'python'
nova_string = nome[4]
print(nova_string)
#ASCII
print('a' == 'b')
print('b' != 'a')
print('a' > 'X')
print('a' > '1')

for i in range(122):
    print(str(i) + " - "+chr(i))