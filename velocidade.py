velocidade = float(input('\033[1;34m Qual é a velocidade atual do carro?  '))
if velocidade > 80:
    print('\033[1;31mMULTADO você excedeu a velociade permitida que é de 80 Km/h')
    multa = (velocidade - 80)*7
    print(
        '\033[1;32mVocê deve pagar pela multa a quantia de R$ {:.2f} reais'.format(multa))
print('\033[1;33mTenha um bom dia! Dirija com segurança!')
