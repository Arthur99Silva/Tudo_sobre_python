"""
Trabalhando com deltas de data e hora

delta = data final - data inicial

"""

import datetime

data_hj = datetime.datetime.now()

aniversario = datetime.datetime(2024, 3, 3, 0)

tempo_para_evento = aniversario - data_hj

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)
