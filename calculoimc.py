'''Calculo do IMC'''

peso = float(input('Qual é o seu peso? (kg)  '))
altura = float(input('Qual é a sua altrua? (m) '))
imc = peso / (altura * altura)
print('O IMC desta pessoa é de \033[1;32m{:.1f} '.format(imc))
if imc < 18.5:
    print('\033[1;34mVocê está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('\033[1;32mPARABÉNS, você esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('\033[1;36mVocê esta em SOBREPESO')
elif 30 <= imc < 40:
    print('\033[1;33mVocê esta em OBESIDADE!')
elif imc > 40:
    print('\033[1;31mVocê esta em OBESIDADE MÓRBIDA, cuidado')
