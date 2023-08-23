"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto, Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python,dividimos os métodos, em 2 grupos: Métodos de instância
e Métodos de Classe.

1) Métodos de instância

0 metodo dunder init __init__ e um metodo especial chamado de construtor e sua função é construir o objeto
a partir da classe.

OBS: Os métodos/ funções dunder em Python sâo chamados de métodos mágicos.
ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no inicio e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da I àn ua em. Então, evite ao máximo.

Baixe a biblioteca -> pip install passlib

2) Métodos de classe

Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens.

"""

# 1) Métodos de instância

"""
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class Conta:
    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = Conta.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        Conta.contador = self.__numero


class Produto:
    contador = 5000

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.id
#Retorna o valor do produto com desconto
    def desconto(self, porcentagem):
        
        return(self.__valor * (100 - porcentagem))/100

p1 = Produto('PS5', 'Console', 4000)
print(p1.desconto(50))
print(Produto.desconto(p1, 40))


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('Nome:')
sobrenome = input('Sobrenome:')
email = input('Email:')
senha = input('Senha: ')
confirma_senha = input('Confirme a senha:')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha errada..!')
    exit(1)
print('Usuário criado!')

senha = input('Digite a senha p/ acesso:')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado!')

print(f'Senha user cripitografado: {user._Usuario__senha}') #Acesso errado

"""

# 1) Métodos de classe

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user = Usuario('Arthur', 'Antunes', 'arthu@gmail.com', '1234')
Usuario.conta_usuarios()
