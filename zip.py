"""
Zip

zip() -> Cria um iterável(Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

"""
print('----Exemplo 1----')
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionário
print(list(zip1))
zip1 = zip(lista1, lista2)
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip
print('----Exemplo 2----')

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zp = zip(tupla, lista, dicionario.values())
print(list(zp))

# Listas de tuplas
print('----Exemplo 3----')
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

print('----Exemplo 4----')
prova1 = [81, 90, 78]
prova2 = [98, 89, 53]
alunos = ['pedro', 'ana', 'teo']

#zip3 = zip(prova1, prova2, alunos)
#print(list(zip3))

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
