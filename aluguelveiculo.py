d= int(input('Digite quantos dias você usou o veiculo?: '))
k = float(input('Digite a quantidade de quilomentos que você rodou no veiculo? Km '))
p = d * 60 + k * 0.15
print('A quantia que você tem que pagar por ter rodado {:.2f} km e usado {:.0f} dias  é de R$ {:.2f}: '.format(k, d, p))