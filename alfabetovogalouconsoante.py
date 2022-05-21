from tokenize import Number


print('''Para saber se uma letra digitada é vogal ou consoante''')
alfa = str(input("Informe UMA letra ou consoante do alfabeto: ")).upper()

if alfa == "A" or alfa == "E" or alfa == "I"or alfa == "O" or  alfa == "U":
    print(f"A letra {alfa} é uma Vogal")
    
elif alfa == "0" or alfa == "1" or alfa == "2" or alfa == "3" or alfa == "4" or alfa == "5" or alfa =="6" or alfa == "7" or alfa == "8" or alfa == "9":
    print("Digite uma letra o valor que você inseriu não é válido")
else:
    print(f"A letra {alfa} é uma Consoante")
    

