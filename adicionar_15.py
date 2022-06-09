#m = int(input('Digite um valor que você conseguiu durante a semana: '))
def adiciona_15 (m):
    if m >= 100:
        m +=15
        print(f'o valor de {m}') 
    else:
        print(f'Guarde mais dinheiro Pedro')
        
        
adiciona_15(120)


def mais_nove(a):
    return (a + 9)


print('O valor da função mais nove é : ',mais_nove(50))  
print(adiciona_15(120) , mais_nove(60))      