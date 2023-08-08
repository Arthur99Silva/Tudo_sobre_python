"""
Listas Aninhadas(Nested Lists)

Algumas linguagens de programação(C/Java) possuem uma estrutura de dados chamada de arrays:

- Unidimensionais(Vetores);
-Multidimensionais(Matrizes);

Em Python nós temos as Listas
"""
print('----Exemplo 1----')
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados
print('Acesso a um dado da lista')
print(listas[0][2]) # Acessa o numero 3

# Iterarando com loops em uma lista aninhada
print('Iterando')
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
print('List Comprehension')
[[print(valor) for valor in lista] for lista in listas]

print('----Exemplo 2----')
print('Gerando tabuleiro 3 x 3')
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para jogo de velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
