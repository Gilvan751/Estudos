print('PROGRAMA PARA CALCULAR A MÉDIA DE UM ALUNO')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2
if m < 5:
    print(
        'Sinto muito mais sua média foi {:.1f} é você esta REPROVADO!'.format(m))
elif 5 <= m < 7:
    print('Sua media foi {:.1f} é o você esta de RECUPERAÇÃO!'.format(m))
else:
    m >= 7
    print('Parabéns sua média foi {:.1f} e você foi APROVADO!'.format(m))
