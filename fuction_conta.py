def conta(numeros):
    total = 0
    for x in numeros:
        if x <= 80:
            total +=1
    return total
    
lista = [1,3,7,8,29,27,26,98]
    
print(conta(lista))