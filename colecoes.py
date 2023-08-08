# Listas aceitam valore duplicados, então temo 10 elementos
lista = [99, 2, 34, 13, 2, 12, 23, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')
print('______________________________________________________________________________')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 13, 2, 12, 23, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')
print('______________________________________________________________________________')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 13, 2, 12, 23, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
print('______________________________________________________________________________')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 13, 2, 12, 23, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
print('______________________________________________________________________________')
