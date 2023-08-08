"""
Funções de maior Grandeza - HOF

Quando uma linguagem suporta HOF, indica que podemos ter funções que retornam outras funções como resultado
ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo crair variáveis do tipo
de funções em nossos programas.

Em Python podemos ter funções dentro de funções, que são conhecidas de Nested Functions ou Funções Aninhadas
ou Inner Functions. Elas podem acessar o escopo de funções mais externas.

"""
print("----Exemplo 1 -  Definindo as funções----")


def somar(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(calcular(4, 2, somar))
print(calcular(4, 2, subtracao))
print(calcular(4, 2, multiplicar))
print(calcular(4, 2, dividir))

print('----Exemplo 2 - Nested Functions----')
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Saia daqui', 'Gostei'))

    return humor() + pessoa


print(cumprimento('Arthur'))
print(cumprimento('Antunes'))

print('-----Exemplo 3 - Retornando funções de outras funções----')


def faz_rir():
    def rir():
        return choice(('kkkkkkk', 'rsrsrsrsrs', 'lololololol'))

    return rir


rindo = faz_rir()
print(rindo())


def faz_rir_novamente(pessoa):
    def rindo_dnv():
        risada = choice(('hahahahaha', 'rsrsrsrsrs', 'jajajajajaja'))
        return f'{risada} {pessoa}'

    return rindo_dnv


rindo = faz_rir_novamente('Arthur')
print(rindo())
print(rindo())
print(rindo())
