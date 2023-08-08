"""
Min e Max

max() -> Retorna o maior valor em um iterável ou maior de dois ou mais elementos.

min() -> Retorna o menor valor em um iterável ou menor de dois ou mais elementos.
"""
print('----Exemplo max 1----')
lista = [1, 8, 4, 99, 34, 129]  # Será assim em todas as coleções
print(max(lista))  # 129

print('----Exemplo max 2----')
# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor:'))
val2 = int(input('Informe o segundo valor:'))

print(max(val1, val2))

print('----Exemplo min 1----')
lista = [1, 8, 4, 99, 34, 129]  # Será assim em todas as coleções
print(min(lista))  # 129

print('----Exemplo min 2----')
# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor:'))
val2 = int(input('Informe o segundo valor:'))

print(min(val1, val2))

print('----Exemplo 1----')
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim


