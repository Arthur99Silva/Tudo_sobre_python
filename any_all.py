"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio. Verifica se
         os elementos são True.
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.

"""
print('----Exemplo 1 all----')

print(all([1, 2, 3, 4])) # Todos os números são verdadeiros? True
print(all([0, 1, 2, 3, 4])) # False
print(all([])) # True

print('----Exemplo 2 all----')
nomes = ['Carlos', 'Camila', 'Cris', 'Carla', 'Cezar']
print(all([nome[0] == 'C' for nome in nomes]))

print('----Exemplo 1 any----')

print(any([1, 2, 3, 4])) # Todos os números são verdadeiros? True
print(any([0, 1, 2, 3, 4])) # True
print(any([])) # False

print('----Exemplo 2 any----')
nomes = ['Carlos', 'Camila', 'Cris', 'Carla', 'Cezar']
print(any([nome[0] == 'C' for nome in nomes]))
