n = s = media = cont =0
while True:
    n = int(input("Digite um numero inteiro: "))
    if n == 999:
        break
    s += n
    cont += 1
    m = s / cont
print(f'A soma vale  {s} e a média vale {m:.2f}')
    