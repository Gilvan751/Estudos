
print('{:-^40}'.format("SUPER BARATÃO"))
total = totmil = menor = cont =   0
produto = ''
while True:
    nome = str(input('Nome produto:  '))
    preco = float(input('Digite o valor do Produto:R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? :[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format("FIM DO PROGRAMA"))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00 reais')
print(f'O produto mais barato foi {barato} e cutou R$ {menor:.2f}')
print('{:-^40}'.format("-=-"))

