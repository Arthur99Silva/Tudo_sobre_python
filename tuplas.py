"""
Tuplas

São bastante parecidas com listas. Existem 2 diferenças básicas:

1 - As tuplas são representadas por parênteses ();
2 - São imutáveis, isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla;

"""
# Cuidado 1: as tuplas são representadas por parêntese, mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))
print('___________')

# Cuidado 2: tuplas com 1 elemento
tupla3 = (4) # N é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Issp é uma tupla
print(tupla4)
print(type(tupla4))

tupla = tuple(range(11))
print(tupla)
print(type(tupla))
print('___________')

# Desempacotamento de tuplas
tupla5 = ('Arthur', 'Antunes')
nome, sobrenome = tupla5
print(nome)
print(sobrenome)
print('___________')

# Métodos para adição e remoção de elementos em tplas não existem, dado o fato das tuplas serem imutáveis

# Soma*, Valor máximo* e mínimo*, e tamanho
# * Se os valores forem todos inteiros ou reais

tupla6 = (1, 2, 3, 4, 5, 6)
print(sum(tupla6))
print(max(tupla6))
print(min(tupla6))
print(len(tupla6))
print('___________')

# Concatenação de tuplas

tupla7 = (1, 2, 3)
print(tupla7)

tupla8 =(4, 5, 6)
print(tupla8)

print(tupla7 + tupla8)

print(tupla7)
print(tupla8)

tupla9 = tupla7 + tupla8
print(tupla9)
print('___________')
# Verificar elementos em uma tupla

print(3 in tupla6)
print('___________')

# Iterando em uma tupla

for n in tupla7:
    print(n)

for indice, valor in enumerate(tupla7):
    print(indice, valor)

print('___________')

# Contando elementos dentro de uma tupla

tupla10 = ('a', 'r', 't', 'a', 'y')
print(tupla10.count('a'))

pessoa = tuple('Arthur')
print(pessoa)

print(pessoa.count('r'))
print('___________')

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados em uma coleção

# Por que utilizar tuplas?
# 1 - Tuplas são mais rápidas do que listas;
# 2 - Deixam o código mais seguro, pois trabalhar com elementos imutáveis traz mais segurança;
