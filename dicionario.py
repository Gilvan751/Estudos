''' alfabeto = {"a":"apartamento", "b":"Barateiro"}
alfabeto1 = {1:10,2:20,3:30}
alfabeto2 = {5.5:50,6.5:60}
alfabeto3 = {(10,20):["apartamento","Barateiro",100]}
print(alfabeto3)
print(type(alfabeto3))
print(alfabeto["b"])
print(alfabeto.get('d', 'Valor nao encontrado')) '''
           #keys       values
''' agenda = {992258112:"Maria",99697854:"Pedro",648794512:"Marieta",62987451236:"Julio"}
print(agenda)
del(agenda[62987451236])
print(agenda)
print(agenda.keys())
print(agenda.values())
print(len(agenda))
print(agenda.popitem())
print(agenda.popitem())
print(agenda) '''
dias_semana = {'dia1': 'domingo', 'dia2': 'segunda-feira', 'dia3': 'terça-feira',
               'dia4': 'quarta-feira', 'dia5': 'quinta-feira', 'dia6': 'sexta-feira', 'dia7': 'sabado'}
print(dias_semana.popitem())
#del(dias_semana['dia7'])
print(dias_semana)
print(dias_semana.popitem())
#del(dias_semana['dia6'])
print(dias_semana)
del(dias_semana['dia2'])

print(dias_semana.keys())
print(dias_semana.values())
print(dias_semana)
