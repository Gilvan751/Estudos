p = float(input('Digite o valor do produto R$: '))
d = p * 0.05
t = p - d
print('O preço do pruduto que custa R${} com desconto de 5% que equivale a R${:.2f} você pagara apenas R${:.2f}'.format(p, d, t))