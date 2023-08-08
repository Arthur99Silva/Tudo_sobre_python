"""
Módulo Collections - Named Tuple

São tuplas, diferenciadas, onde, escificamos um nome para a mesma e também parâmetros.
"""
print('-TUPLA NORMAL-')
tupla = (1, 2, 3)
print(tupla[1])

print('-NAMED TUPLE-')
from collections import namedtuple

# Definido o nome e os parâmetros
# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade = 2, raca = 'Vira-lata', nome = 'Ray')

print(ray)
