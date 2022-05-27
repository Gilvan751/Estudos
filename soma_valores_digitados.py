num = cont = soma = media = 0

while num != 999:
    num = int(input('Digite um númeor [999 para parar] '))
    if num == 999:
        break
    soma = soma + num
    cont += 1
    media = soma / cont
    
    
print(f'Você digitou {cont} números e a soma entre eles é {soma} e a média e {media} ')
