resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant +=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    resp = str(input('Quer continumar [S/N]?  ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou a quantidade de {quant} números e a media aritmética foi de: {media:.2f}')
print(f'Temos o maior número  {maior} e o menor número  {menor}')