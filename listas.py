"""
Listas

Listas em Python funcionam como vetores/matrizes/arrayes, com a diferença de serem dinâmicos
e também podermos colocar qualquer tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:
    - Dinâmico: Não possui tamanho fixo; Ou seja podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['A', 'r', 't', 'h', 'u', 'r', ' ', 'a', 's', 's']
lista3 = []
lista4 = list(range(11))
lista5 = list('Arthur Antunes')

# Podemos facilmente checar se determinado valor está contido em uma lista
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista2.count('a'))

# Adicionar elementos em listas, utilizamos a função append. Com append só é possível adicionar um elemento por vez.
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1)

# Extend coloca cada elemento adicional na lista
lista1.extend([1, 4, 7, 33])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice, desloca o valor para a direita
lista1.insert(2, 'Novo valor')
print(lista1)

#  Podemos facilmente juntar duas listas
#lista6 = lista1 + lista2
# print(lista6)
# ou faça
lista1.extend(lista2)
print(lista1)

# Invertendo uma lista
lista5.reverse()
# ou faça
# print(lista5::-1)
print(lista5)

# Copiar uma lista
lista7 = lista2.copy()
print(lista7)

# Contando quantos elemntos tem na lista
print(len(lista1))

# Podemos remover facilmente o ultimo elemento de uma lista
print(lista7)
lista7.pop()
print(lista7)

# Podemos remover o elemento pelo indíce
lista7.pop(3)
print(lista7)

# Zerando a lista
#lista7.clear()

# Repetindo elementos da lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Convertendo uma string em uma lista
curso = 'Udemy Python'
curso = curso.split()
print(curso)
# O split separa os elementos por espaço, podendo definir qual é o separador. Ex.: split(',')

# Abaixo estamos falando: pega a lista8, coloca espaço entre cada elemento e transforma em string
lista8 = ['Esse, curso, Python']
print(lista8)
curso = ' '.join(lista8)
print(curso)

"""
# Iterando sobre listas
# Exemplo com for
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo com while
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicionar um produto na lista ou digite sair:')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

# Variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Fazendo acesso de elemntos de forma indexada
#       0       1       2       3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
print('_______________')

for cor in cores:
    print(cor)
print('____________')

indice = 0
# Indice em while
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
print('___________')

for indice, cor in enumerate(cores):
    print(indice, cor)

print('____________')

# Encontra indice de um elemento em uma lista
num = [12, 23, 56, 98]
print(num.index(23))

# Tranformar lista em tupla
l = [1, 2, 3, 4, 5, 6]
print(l)
print(type(l))

tupla = tuple(l)
print(tupla)
print(type(tupla))
