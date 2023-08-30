"""
Trabalhando com JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube... ) e terceiros (nós desenvolvedores).

- Exemplo 1

import json

ret = json.dumps(['produtos', {'PS5': ('2TB', 'Novo', '220V', 3300)}])

print(type(ret))

print(ret)

- Exemplo 2

import json


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

Integrando JSON com Pickle

pip install jsonpickle
"""

import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

