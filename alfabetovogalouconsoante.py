from tokenize import Number


print('''Para saber se uma letra digitada é vogal ou consoante''')
alfa = str(input("Informe uma letra ou consoante do alfabeto: ")).upper()

if alfa == "A" or alfa == "E" or alfa == "I"or alfa == "O" or  alfa == "U":
    print(f"A letra {alfa} é uma Vogal")
    
   
else:
    print(f"A letra {alfa} é uma Consoante")
    

