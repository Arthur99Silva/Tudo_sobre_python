"""
POO -> Atributos

Representam as caracteristicas do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente
os estados de um objeto.

São divididos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

1) Atributos de instância: São atributos declarados dentro do método construtor(método especial usado para construção
                           do objeto)

Em Python, todo atributo de classe é público. Ou seja pode ser acessado em todo projeto. Caso queiramos mostrar que um
atributo deve ser tratado como privado, ou seja, só pode ser acessado dentro da própria classe, utiliza __ no início do
seu nome.

O que significa atributos de instância?
Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

2) Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
fora do contrutor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
terão o mesmo valor para este atributo.

3) Atributos dinâmicos - > Um atributos de instância que pode ser criado em tempo de execução.
OBS: O atributo dinâmico será exclusivo da instância que o criou.
"""


# 1) Atributos de instância


class Lampada:

    def __init__(self, volts, cor):
        self.volts = volts
        self.cor = cor
        self.ligada = False


class Conta:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos e privados

class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)


# Exemplo

user = Acesso('user@gmail.com', '12345')
# print(user.email)

user.mostra_senha()


# 2) Atributos de classe
# Refatorar a classe Produto


class Produto:
    imposto = 1.05  # 0.05% de imposto -> Atributo de classe
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PS5', 'Console', 4000)
p2 = Produto('Xbox Series X', 'Console', 3800)

print(p1.imposto)  # Acesso posnvcl, mas 1 ncorreto dc um atributo de classe
print(p2.imposto)  # Acesso posnvcl, mas 1 ncorreto dc um atributo de classe
# OBS: Não precisamos crlar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)


# 3) Atributos dinâmicos


p3 = Produto('Arroz', 'Comida', 5.99)

# Criando um atributo dinâmico em tempo de execução

p3.peso = '5kg' # Note que na classe Produto não existe o atributo peso
print(f'Produro: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')

# Deletando atributos

# print(p1.__dict__)
