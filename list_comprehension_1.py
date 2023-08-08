"""
List Comprehension - Parte 1

- Utilizando List Comprehension, podemos gerar novas listas com dados processados a partir de outro iterável.

- Sintaxe:
    [dado for dado in iterável]
"""
print('----Exemplo 1----')
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)
"""
Para entender melhor o que está acontecendo devemos dividir a ecpressão em duas partes:
1 - for numero in numeros
2 - numero * 10
"""
res =[numero/2 for numero in numeros]
print(res)


def func(valor):
    return valor * valor

res = [func(numero) for numero in numeros]
print(res)

# List comprehension versus Loop
print('----Exemplo 2----')
print('Usando Loop:')
num = [1, 2, 3, 4, 5]
num_dobrados = []
for num in numeros:
    num_dobro = num * 2
    num_dobrados.append(num_dobro)

print(num_dobrados)

print('Agora usando List comprehension:')
print([num * 2 for num in numeros])

print('----Exemplo 3----')
nome = 'Arthur Antunes'
print([letra.upper() for letra in nome])

"""
Nós podemos adicionar estruturas condicionais lógicas ás nossas List Comprehension
"""
print('----Exemplo 4----')

lista_num = [1, 2, 3, 4, 5, 6]
pares = [lista_n for lista_n in lista_num if lista_n % 2 == 0]
impares = [lista_n for lista_n in lista_num if lista_n % 2 != 0]

print('Pares')
print(pares)
print('Impares')
print(impares)

print('Refatorando')
# Qualquer número par módulo de 2 é 0 e 0 em Python é False. Not False = True
pares = [lista_n for lista_n in lista_num if not lista_n % 2]
# Qualquer número ímpar módulo de 2 é 1 em, e 1 em Python é True
impares = [lista_n for lista_n in lista_num if lista_n % 2]

print('Pares')
print(pares)
print('Impares')
print(impares)
