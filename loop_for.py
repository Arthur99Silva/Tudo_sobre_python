"""
Loop For

Exemplo em Python:

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
-String:
    nome = 'Arthur'

-Lista:
    lista = [1, 3 ,4 ,5 ,8]

-Range:
    numeros = range(1, 10)

nome = 'Arthur Antunes'
lista = [1, 3 ,4 ,5 ,8]
numeros = range(1, 10) # Temos que transformar em uma lista

#Exemplo de for 1
for letra in nome:
    print(letra)

for letra in nome:
    print(letra, end='')

#Exemplo de for 2
for numero in lista:
    print(numero)

#Exemplo de for 3

range(valor_inicial, valor_final)
Obs: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 -> Não

for numero in range(1, 10):
    print(numero)

#Enumerate -> ((0, 'A'), (1, 'r'), ...
for indice,letra in enumerate(nome):
    print(nome[indice])

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
    numero = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + numero
print(f'A soma é {soma}')
"""

