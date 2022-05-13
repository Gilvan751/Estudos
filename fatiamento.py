frase = 'Curso em Video Phyton'
print(frase)
print(frase[9]) #fatia ou apresenta a frase 9 no caso aqui e o V
print(frase[9:20]) #inicia no  9 e vai ate o 19
print(frase[3:13])
print(frase[:6])
print(''' Para escrecer um texto
todo na tela sem se preocupar com 
o modelo e quantidade de texto basta colocaar
tres aspas simples ou duplas
que o texto sera escrito''')
print(frase[::2]) #salta de duas em duas
print(frase[9::2])
print(len(frase)) # conta a quantidade de letras da frase com espaços
print(frase.count('o')) #conta quantos 'o' aparece na frase
print(frase.upper().count('o')) #pode combinar utilizar propriedade dentro de propriedade de uma vez so para mudar a situação da frase
print(frase.count('o',0,13)) #vai indicar quantos 'o' tem entre 0 e 13 lembrando que ele exclui o 13
print(frase.find('deo')) #vai indicar onde começa a frase deo
print(frase.find('Android')) #vai indicar quantas ocorrencias tem a palavra Android dentro da frase
print(frase.replace('Video', 'Android')) # Troca o nome da variavel por outra
print('Curso'in frase) # vai dizer com o 'in' que se tem vai aparecer True se não False
print(frase.upper()) #transforma tudo em maiuscula
print(frase.lower()) #transforma tudo em minuscula
print(frase.capitalize()) #Transforma a primeira letra da sentença em maiuscula
print(frase.title()) #Transforma a primeira letra de cada sentença em maiuscula
print(frase.strip())
print(frase.split())
print('-'.join(frase)) #Faz a junção da palavra separado pelo tipo de separador que voce colocou
a = '   Apreda Phyton   '
print(a.split()) # gera uma lista os termos da string
print(a.strip()) #tira os espaços que a pessoa começou a digitar depois em um input
print(a.rstrip()) #remove os espaços da direita
print(a.lstrip()) #remove os espaços da esquerda