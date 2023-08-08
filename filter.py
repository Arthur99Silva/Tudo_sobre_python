"""
Filter

filter() -> Serve para filtar dados de uma determinada coleção.

Diferença entre map() e filter():
 - map(): Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do
          iterável;
- filter(): Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
            acordo com a função;
"""
import statistics
print('----Exemplo 1----')

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilzando a função mean()
media = statistics.mean(dados)

print(f'Média foi de  {media}')

res = filter(lambda x: x > media, dados)
print(list(res))

print('----Exemplo 2----')

paises = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', ' Equator', '', '', 'Venezuela']

print(paises)

#ress = filter(None, paises)
#ress = filter(lambda pais: len(pais) > 0, paises)
ress = filter(lambda pais: pais != '', paises)

print(list(ress))

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

# Filtrar os usuários inativos no Twitter

#inativos = list(filter(lambda u: len(u["tweets"]) == 0, usuarios)) -> FORMA 1

inativos = list(filter(lambda u: not u["tweets"], usuarios)) # -> FORMA 2

print(inativos)

# Combinar filter() e map()
print('----Exemplo 4----')

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo "Sua instrutora é" + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
