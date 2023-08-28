"""
POO - Herança

A ideia de herança é a de reaprovei tar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

OBS: Quando uma Classe herda de outra ela herda TODOS os atributos métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;

Quando uma classe herda de outra classe,ela é chamada:
    [Cliente, Funcionarioj
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Arthur', 'Antunes', '123456-78', 5000)
funcionario1 = Funcionario('Arthur', 'Silva', '9999999', 5000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
