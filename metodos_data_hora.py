"""
Métodos de datas e horas

Formatando datas / horas com strftlme() (Stnng Forrnat 11me) -> dd/mm/yyy hora: minuto
"""

import datetime
import timeit

agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))
print('________________________________________')

# Mudanças ocorrendo á meia-noite conine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())
print('________________________________________')

aniversario = input('Data do seu aniversário:')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda-feira!')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terca-feira!')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta-feira!')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta-feira!')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta-feira!')
elif aniversario.weekday() == 5:
    print('Voce nasceu em uma sabado-feira!')
elif aniversario.weekday() == 6:
    print('Voce nasceu em uma domingo-feira!')

print('________________________________________')

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)