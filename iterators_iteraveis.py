"""
Entendendo Iterators e Iteráveis

Iterator:
    - Um objeto que pode ser iterado;
    - Retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iteráveis:
    - Um objeto que retorna um iterator quando a função iter() é chamada;
"""
nome = 'Arthur'  # É um iterável mas não é um interator
num = [1, 2, 3, 4, 5]  # É um iterável mas não é um interator

it1 = iter(nome)
it2 = iter(num)

# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))

# print(next(it2))
# print(next(it2))
# print(next(it2))
# print(next(it2))
# print(next(it2))

for letra in nome:
    print(f'{letra}')

