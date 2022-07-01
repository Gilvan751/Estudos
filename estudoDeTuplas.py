times = ('Palmeiras','Corinthians','Athletico-PR','Internacional','Atlético-MG','Fluminense'
         ,'Santos','São Paulo','Flamengo','Botafogo','Avaí','Bragantino','Atlético-GO'
         ,'Goiás','Ceará','Coritiba','América-MG','Cuiabá','Juventude','Fortaleza')
print('=-'*15)
print(f'Lista dos times:{times} ')
print('=-'*15)
print(f'Os 5 primeiro times são: {times[0:5]}')
print('=-'*15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=-'*15)
print(f'A lista dos times organizados por ordem alfabetica: {sorted(times)}')
print('=-'*15)
print(f'O time do Cuiaba esta na {times.index("Cuiabá") +1}ª posição')