"""
Funções com retorno

"""
numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop : {ret_pop}')
ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')
print('-----------------')

print('----Exemplo 1----')


def quadrado_sete():
    return 7 * 7


ret = quadrado_sete()

print(f'Retorno: {ret}')
print('-----------------')

print('----Exemplo 2----')


def diz_oi():
    return 'oi!'


alguem = 'Pedro'
print(diz_oi() + alguem)
print('-----------------')

"""
Return:
1 - Finaliza a função, ou seja, ela sai da execução da função; -> ex 3
2 - Podemos ter em uma função diferentes returns; -> ex 4
3 - Podemos em uma função qualquer tipo de dado e até mesmo múltiplos valores; -> ex 5
"""

print('----Exemplo 3----')


def diz_ola():
    print('Execução antes do return...')
    return 'OLÁ'
    #print('Execução depois do return...') -> Nunca será executado


print(diz_ola())
print('-----------------')
print('----Exemplo 4----')


def nova_funcao():
    variavel = True # Se mudar True para None será retornado 3.2, se mudar para False irá retornar b
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())
print('-----------------')
print('----Exemplo 5----')


def outra_funcao():
    return 2, 3, 4, 5


#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para cara e coroa
print('-----------------')
print('----Exemplo 6----')
from random import random


def joga_moeda():
    # Gera um número pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
