viajem = float(input('Digite a distância de sua viagem? '))
if viajem <= 200:
    viajem = viajem * 0.50
    print(
        '\033[1;32mO valor a ser pago por sua viagem  é de \033[1;33mR$ {:.2f}'.format(viajem))
else:
    viajem = viajem * 0.45
    print(
        '\033[1;32mO valor a ser pago por sua viagem é de \033[1;33mR$ {:.2f}'.format(viajem))
print('\033[1;34mBOA VIAGEM!')
