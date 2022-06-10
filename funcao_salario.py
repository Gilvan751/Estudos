def salario(hrs_traba):
    return hrs_traba * 40

def cont_bonus(hrs_traba):
    return salario(hrs_traba) + 80
print(salario(8), cont_bonus(8))
