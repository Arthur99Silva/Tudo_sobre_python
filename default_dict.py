"""
Módulo Collections - Default Dict

Ao criar um dicionário utilizando o Default Dict, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.

"""
print('____Dicionário normal_____')
dicionario = {'curso': 'Programação'}
print(dicionario)
print(dicionario['curso'])
print('___________________________')

# Fazendo import
print('____Default Dict____')

from _collections import defaultdict

dicionario2 = defaultdict(lambda: 0)

dicionario2['curso'] = 'Programação'
print(dicionario2)

print(dicionario2['outro']) # Em um dicionário comum daria KeyError
print(dicionario2)
