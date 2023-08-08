"""
Generators

São as Tuple Comprehension

O exemplo a seguir pode ser feito usando generators:

nomes = ['Carlos', 'Camila', 'Cris', 'Carla', 'Cezar']
print(all([nome[0] == 'C' for nome in nomes]))

"""
print('----Exemplo 1----')
nomes = ['Carlos', 'Camila', 'Cris', 'Carla', 'Cezar', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generators
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

print('----Exemplo 2----')

from sys import getsizeof # getsizeof retorna a quantidade de bytes em memória do elemento passado como parâmetro

print(getsizeof('Arthur Antunes'))

print('----Exemplo 3----')

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generators
gen = getsizeof((x * 10 for x in range(1000)))

print('Memória gasta em cada tarefa: ')
print(f'List Comrehension -> {list_comp}')
print(f'Set Comrehension -> {set_comp}')
print(f'Dictionary Comrehension -> {dict_comp}')
print(f'Generator -> {gen}')

