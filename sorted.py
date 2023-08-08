"""
Sorted

O sorted() pode ser usado em qualquer iterável. Serve para ordenar elementos.
O sorted sempre retorna uma lista. com os elementos ordenados.

"""
print('----Exemplo 1----')
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))  # Menor para o maior
print(numeros)

print('----Exemplo 2----')
num = [6, 1, 8, 2]

# Adicionando parâmetros ao sorted()
print(sorted(num, reverse=True))  # Maior para menor

print('----Exemplo 3----')

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu amo pizza"]},
    {"username": "Carla", "tweets": ["SIIIM"]},
    {"username": "Pedro", "tweets": []},
    {"username": "Raul", "tweets": []},
    {"username": "Marcelo", "tweets": ["Bolosssss", "PIZZAAAA"]},
    {"username": "Ana", "tweets": []}
]
print(usuarios)
print('ORDENANDO...')
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

print('----Exemplo 4----')

musica = [
    {"titulo": "Musica A", "tocou": 3},
    {"titulo": "Musica B", "tocou": 15},
    {"titulo": "Musica C", "tocou": 6},
    {"titulo": "Musica D", "tocou": 32}
]

print("--Da menos tocada para a mais tocada--")
print(sorted(musica, key=lambda musica: musica["tocou"]))

print('--Da mais tocada para a menos tocada--')
print(sorted(musica, key=lambda musica: musica["tocou"], reverse=True))
