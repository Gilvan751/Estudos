nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em letras maiusculas é {} '.format(nome.upper()))
print('Seu nome completo em letras minusculas é {} '.format(nome.lower()))
print('Seu nome tem a quantidade total de  {} letras'.format(len(nome.replace(' ',''))))

#.strip no inicio elimina os espaços em branco no inicio e fim do nome
#a terceira funçao poderia ser .format(len(nome) - nome.count(' ')
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))