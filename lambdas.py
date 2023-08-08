"""
Utilizando Lambdas

São funções sem nome, ou seja, funções anônimas.

"""
print('----Exemplo 1----')
print('Função Python')


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print('Expressão Lambda')

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1
print(calc(4))

print('----Exemplo 2----')
# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' arthur', 'antunes'))

print('----Exemplo 3----')
# Lambda sem nenhuma entrada

func = lambda: 'Eu sou Arthur'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

print(func())
print(uma(2))
print(duas(2, 4))

print('----Exemplo 4----')
autores = ['Issac Aimov', 'Ray Bradbory', 'Robert Heinlein', 'Arthur C. Doyle', 'H. G. Wells']

print(autores)

autores.sort(key=lambda sobren: sobren.split(' ')[-1].lower())# Ordenação pelo sobrenome

print(autores)

print('----Exemplo 5----')
print('Função quadrática')
#f(x) = a * x ** 2+ b * x + c


def geradora_quadratica(a, b, c):
    """Retorna #f(x) = a * x ** 2+ b * x + c"""
    return lambda x: a * x ** 2+ b * x + c


teste = geradora_quadratica(2, 3, -5)
print(teste(0)) # -> valor de x
print(teste(1))
print(teste(2))

print(geradora_quadratica(3, 0, 1)(2))
