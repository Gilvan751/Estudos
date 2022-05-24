''' lista = [100, 200, 300, 400, 500, 600, 700, 800]
for i in range(len(lista)):
    print(lista[i])
print(lista)
print(lista[3]) '''

#fatianto lista
'''       #   0 1 2
lista = [2,3,4]
        #-3-2-1
nova_lista = lista[0:2:2]
print(nova_lista) '''

''' lista2 = ["p","y","t","h","o","n"]
nova_lista2 = lista2[::-1]
print(nova_lista2) '''

''' lista = ["P","Y","T","H","O","N"]
print(lista)
nova_lista = lista[3:6]
print(nova_lista) '''
''' 
animais = ['Porco', 'Cachorro','Elefante','Coelho']
print(animais)
animais.append('Galinha')#adiciona um elemento na lista
print(animais)
animais.remove('Porco')#remove um elemento da lista que tem que passar qual é
print(animais)
animais.insert(0,'Papagaio')#insere um elemento na lista de acordo com a posição definida inicialmente
print(animais)
# insere um elemento na lista de acordo com a posição definida inicialmente
animais.insert(6, 'Cavalo')
print(animais)#remove o elemento da lista comforme a posição passada
animais.pop(0)
print(animais)
animais.pop(3)
print(animais)
 '''
 
''' lista = ['a','d','e','a','y','w', 'i','j','ç']
#pode usar o comando 
for i in range(len(lista)):
     print(lista[i])
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
l = lista.count('a')
print(l) '''

moveis = ['Geladeira','Fogão','Sofá','Mesa']
moveis.append('TV')
print(moveis)
moveis.pop(2)
print(moveis)