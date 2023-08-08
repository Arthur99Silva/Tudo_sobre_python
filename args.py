"""
Entendendo *args

- O *args é uma parâmetro, como outro qualquer. Isso significa que vc poderá chamar de qualquer coisa,
  desde que comece com *.

Exemplo: *xis

Mas por convenção, utilizamos *args para definí-lo. O parâmetro *args utilizado e uma função, coloca os
valores extras informados como entrada em uma tupla. Então lembre-se que tuplas são imutáveis.
"""
print('----Exemplo 1----')


def soma_numeros(*args):
    return sum(args) # Assim é melhor
    #total = 0
    #for numero in args:
        #total = total + numero
    #return total

print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(2, 3))
print(soma_numeros(2, 3, 4))

print('----Exemplo 2----')


def verifica(*args):
    if 'Arthur' in args and 'Antunes' in args:
        return 'Bem vindo Arthur'
    return 'Não é você...'


print(verifica())
print(verifica(1, True, 'Antunes', 'Arthur'))
print(verifica(1, 'Antunes', 3.145))

print('----Exemplo 3----')


def soma(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5]
# Desempacotador da lista
print(soma(*numeros))
# O * significa que esta sendo passado uma coleção de dados
