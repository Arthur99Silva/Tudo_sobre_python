"""
Manipulando data e hora

Python tem um modulo built -in (integrado) para se trabalhar com data e hora
chamado datetime


"""

import datetime

#print(datetime.MAXYEAR)
#print(datetime.MINYEAR)

# Data e hora corrente
#print(datetime.datetime.now())
#print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0 min, 0 seg, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

print('___________________________________________')

evento = datetime.datetime(2024,1,1)
print(type(evento))
print(type('31/12/2023'))

nascimento = input('Informe data de nascimento:')

nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
print()
