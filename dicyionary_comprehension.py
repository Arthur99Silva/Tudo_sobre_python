"""
Dictionary Comprehension

Um dicionário é:

dicionario = {'a':1, 'b':2, 'c':3}

Sintaxe:

{chave: valor for valor in iteravel}
"""
print('----Exemplo 1----')
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor for chave, valor in numeros.items()}
print(quadrado)

print('----Exemplo 2----')
num = [1, 2, 3, 4, 5]
quad = {valor: valor ** 2 for valor in num}
print(quad)

print('----Exemplo 3----')
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exmplo com lógica condicional
print('----Exemplo 4----')
numbers = [1, 2, 3, 4, 5]
res = {numb: ('par' if numb % 2 == 0 else 'impar') for numb in numbers}
print(res)
