"""
Módulo Collections - Counter(contador)

Collections -> High-perfomance Container Datetypes

Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor
a quantidade de ocorrências deste elemento.

"""

# Utilizando o Counter

from collections import Counter

lista = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 45, 45, 66, 66, 43, 34] # Pode ser qualquer coleção
res = Counter(lista)
print(type(res))
print(res)
