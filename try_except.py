"""
O bloco try/except

Utilizando o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare
de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    // o que deve ser feito em caso de problema

"""
print('----Exemplo 2 - Erro genérico----')
"""Tratar erro de forma genérica não é a melhor forma. O ideal é tratar de forma específica"""
try:
    geek()
except:
    print('Deu algum problema')

print('----Exemplo 2 - Erro específico----')
try:
    geek()
except NameError:
    print('Erro: usando uma função que não existe')

print('----Exemplo 3----')
try:
    len(5)
except TypeError as err:
    print('A aplicação gerou o seguinte erro: {err}')

print('----Exemplo 4----')
try:
    len(5)
except NameError as erra:
    print(f'Deu NameError:{erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')

print('----Exemplo 5----')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {"nome": "Arthur"}
print(pega_valor(dic, "nome"))
