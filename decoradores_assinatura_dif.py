"""
Decoradores com diferentes assinaturas - Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
"""
print('----Exemplo 1----')

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}'


@gritar
def ordenar(pricipal, acompanhamento):
    return f'Olá gostaria de {pricipal} acompanhado de {acompanhamento}'


print(saudacao('Arthur'))

print(ordenar('Picanha', 'Batata'))


@gritar
def lol():
    return 'lol'


print(lol())

print('----Exemplo 2 - Decorator com argumentos-----')


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_fav(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(a, b):
    return a + b


print(comida_fav('arroz', 'pizza'))
print(comida_fav('pizza'))
print(soma_dez(1, 2))
print(soma_dez(9, 1))
