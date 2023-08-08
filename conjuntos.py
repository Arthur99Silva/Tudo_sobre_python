"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência á Teoria dos Conjuntos da Matemática.

- Aqui no Python os conjutos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos são referênciados em Python com chaves {}.

Diferença entre Conjuntos e Mapas:

- Um dicionário(mapa) tem chave e valor;
- Um comjunto tem apenas valor;
"""

# Definindo um Conjunto:
# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos
print(s)
print(type(s))
print('_______________________________________')
"""
OBS: Ao criar um conjunto, caso seja adiocionado um valor existente, o mesmo será ignorado sem gerar error e não fará
parte do conjunto
"""

# Forma 2

c = {1, 2, 3, 4, 5, 5}
print(c)
print(type(c))

if 3 in c:
    print('Tem o 3')
else:
    print('Não tem o 3')
print('_______________________________________')

# Uso interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam a cidade natal. Nós adicionamos cada cidade em uma lista, já que podemos adicionar novos
# elementos e ter repetição.

cidades = ['BH', 'São Paulo', 'Santo André', 'Itaúna','SJDR', 'BH', 'Itaúna', 'BH']
print(cidades)
print(len(cidades))
print('_______________________________________')

# Agora precisamos saber quantas cidades distintas

print(len(set(cidades)))
print('_______________________________________')

w = {1, 2, 3}
w.add(4)
print(w)
print('_______________________________________')

# Remover elementos no conjunto

w.remove(4)
print(w)
print('_______________________________________')

# ou faz

w.discard(2)
print(w)
print('_______________________________________')

# Copiando um conjunto para o outro
z = {1, 2, 3}
print(z)

# Forma 1 - Deep Copy
novo = z.copy()
print(novo)

novo.add(4)
print(novo)
print(z)
print('_______________________________________')

# Forma 2 - Shallow Copy

nv = z
nv.add(4)
print(nv)
print(z)

# Podemos remover todos os itens de um conjunto
x = {1, 2, 3}
print(x)
x.clear()
print(x)
print('_______________________________________')

# Métodos matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um de estudantes de C e um de estudantes de Java

estudantes_c = {'Marcos', 'Ana', 'Ellen', 'Pedro', 'Julia', 'Gui', 'Arthur'}
estudantes_java = {'Fernando', 'João', 'Zé', 'Luan', 'Lucas', 'Julia', 'Arthur'}

# Veja que alguns alunos estudam as duas linguagens

# Precisamos gerar um conjunto com nomes únicos

# Forma 1 - Union
unicos1 = estudantes_c.union(estudantes_java)
print(unicos1)
print('_______________________________________')

# Forma 2 - Caractere pipe -> |
unicos2 = estudantes_c | estudantes_java
print(unicos2)
print('_______________________________________')

# Gerar conjuntos com estudantes em ambos cursos

# Forma 1 - Intersection
ambos1 = estudantes_c.intersection(estudantes_java)
print(ambos1)
print('_______________________________________')

# Forma 2 - &
ambos2 = estudantes_c & estudantes_java
print(ambos2)
print('_______________________________________')

# Gerar um conjunto de estudantes que não estão no outro curso
so_c = estudantes_c.difference(estudantes_java)
print(so_c)
print('_______________________________________')

# Soma*, Valor máximo* e mínimo*, e tamanho
# * Se os valores forem todos inteiros ou reais

q = {1, 2, 3, 4, 5, 6}
print(sum(q))
print(max(q))
print(min(q))
print(len(q))
print('_______________________________________')
