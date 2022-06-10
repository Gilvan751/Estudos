convidados = ['pedro', 'jose', 'maria', 'monica']
convidados[1] = 'Manarino'
del convidados[-1]
convidados.append('Marta')
convidados.append('Joselia')
convidados.append('Martineide')
convidados.remove('Marta')
convidados.extend(['jose', 'manoel', 'Rubia', 'Talisma'])
lista = len(convidados) - 1
print(lista)
print(convidados)
print(f'O primeiro participante é : {convidados[0]}')
print(f'O ultimo participante é : {convidados[8]}')