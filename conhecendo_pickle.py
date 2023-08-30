"""
Conhecendo o Pickle

A função do Pickte é realizar o seguinte processo:

Objeto Python -> Binarizaçào
Binarizaçào -> Objeto Python

Este processo é chamado de serializaçào/deserializaçào

#OBS: O modulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de fontes desconhecidas.
"""

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

"""
#with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato._Animal__nome}')
    gato.mia()
    print(f'O gato chama-se {cachorro._Animal__nome}')
    cachorro.late()

