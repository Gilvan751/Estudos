print('''Conversão de real para dolar''')
cotacaodolar =float(input('Digite o valor da cotação do dolar de hoje '))
real = float(input('Digite o valor em reais  que você quer converter em dolar '))
t = real / cotacaodolar

print(f'O valor de R${real} transformado em dolar na cotação de hoje é US${t:.2f}')

print('''Conversão de dolar para real''')
dolar = float(
    input('Digite o valor em dolares US$ '))


t = dolar *cotacaodolar

print(
    f'O valor de US${dolar} dolares  transformado em reais é R${t:.2f} ')
