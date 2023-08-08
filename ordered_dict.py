"""
Módulo Collections - Ordered Dict

Em um dicionário comum a ordem de elementos não é garantida.
"""
from _collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor{valor}')

print('---Entendendo a diferença entre Dict e Ordered Dict---')

print('-Dicionários comuns-')
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print('-Para o Dict a ordem não importa então será True-')
print(dict1 == dict2)

print('---------------------------------')

print('-Ordered Dict-')
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print('-Para o Ordered Dict a ordem de inserção importa então será False-')
print(odict1 == odict2)
