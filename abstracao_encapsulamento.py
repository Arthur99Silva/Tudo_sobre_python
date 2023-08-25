"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes .

Encapsular -> cápsula

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendoum atributo privado chamado
nome e um método privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso fora da
classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar os elementos
privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.
"""


class Conta:
    contador = 1234

    def __init__(self, titular, limite, saldo):
        self.numero = Conta.contador + 1
        self.titular = titular
        self.limite = limite
        self.saldo = saldo
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de  {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.valor += valor

    def sacar(self, valor):
        self.valor -= valor

# Testando

conta1 = Conta('Arthur', 150, 1500)
print(conta1)
