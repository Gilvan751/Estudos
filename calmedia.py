print('PROGRAMA PARA CALCULAR A MÉDIA')
n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1 + n2) / 2
if m <= 5:
    print('Você esta de recuperação sua média foi {:.1f}'.format(m))
else:
    print('Parabéns você passou sua media foi {:.1f}'. format(m))
print('--FIM--')
