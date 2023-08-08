"""
Reversed

A função reversed() funciona em qualquer iterável. Sua função é inverter o iterável. É retornado um iterável chamado
List Revrsed Iterator

"""
print('----Exemplo 1----')
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print('--Lista--')
print(list(reversed(lista)))

# Tupla
print('--Tupla--')
print(tuple(reversed(lista)))

# Conjunto
print('--Conjunto--')
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
print('----Exemplo 2----')
for letra in reversed('Arthur Antunes'):
    print(letra, end='')

print('\n')
print('-Sem o uso do for-')

print(''.join(list(reversed('Arthur Antunes'))))

# Contagem regressiva usando reversed
print('----Exemplo 3----')
for n in reversed(range(0, 10)):
    print(n)
