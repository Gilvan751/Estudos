'''03 - Se o produto que você quer avaliar custa(??) reais qual
será o valor do mesmo com desconto de(??) % .'''
print(' Calcular o preço de um produto com desconto')
p = float(input('Digite o valor do seu produto R$ '))
d = p * 0.15
t = p - d
print(f'O valor de seu  produto de R$ {p:.2f} reais com o desconto de R$ {d:.2f} reais, você irá pagar apenas a quantia de R$ {t:.2f} reais ')
