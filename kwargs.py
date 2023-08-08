"""
Entendendo o **kwargs

Esse é só mais um parâmetro, mas diferente do *args que coloca valores extras em uma tupla, o **kwargs exige
que parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

Nas funções podem ter(NESTA ORDEM):
- Parâmetros obrigatórios -> *args;
-Parâmetros default -> **kwargs;

"""
print('----Exemplo 1----')


def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}.')


cores_fav(Marcos='verde', Julia='azul', Pedro='amarelo', Lucas='preto')

print('----Exemplo 2----')


def cumprimento(**kwargs):
    if 'Arthur' in kwargs and kwargs['Arthur'] == 'Antunes':
        return 'Arthur te cumprimentou!'
    elif 'Arthur' in kwargs:
        return f"{kwargs['Arthur']} Antunes!"
    return 'Não te conheço...'


print(cumprimento())
print(cumprimento(Arthur='Antunes'))
print(cumprimento(Arthur='Arthur'))

print('----Exemplo 3----')


def minha_funcao(idade, nome, *args, Solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if Solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
print('----')
minha_funcao(18, 'Felipe',4, 5, 3, Solteiro=True)
print('----')
minha_funcao(34, 'Pedro', eu='Não', voce='Vai')
print('----')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

print('----Exemplo 4----')
# Desempacotar **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Arthur', 'sobrenome': 'Antunes'}
print(mostra_nomes(**nomes))

print('----Exemplo 4----')


def soma_num(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_num(*lista)
soma_num(*tupla)
soma_num(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_num(**dicionario)
