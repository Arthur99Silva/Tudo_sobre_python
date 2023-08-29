"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivaçao Direta;
    - Por Multiderivacao Indireta;

CBS: Não importa se a derivaçào ê direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos das super classes.

# Multiderivaçao Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multideriva(Base1, Base2, Base3):
    pass


# Multiderivacao Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multideriva(Base3):
    pass
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou o {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando...'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando...'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} da terra'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())


tux = Pinguim('Tux')
print(tux.nadar())
print(tux.andar())
print(tux.cumprimentar()) # Method Resolution Order




