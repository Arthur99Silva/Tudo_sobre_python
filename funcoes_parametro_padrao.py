"""
Funções com parâmetro padrão (Default parameters)

Usar parâmetros com valor default nos permite ser mais flexíveis, evita erros com parâmetros incorretos, permite
trabalhar com códigos mais legíveis.

- Funções onde a passagem de parâmetros seja opcional;
    ex: printf()

Exemplo 1 -> Se o usuário passar somente um argumento, este será atribuído ao parãmetro número, e será calculado
             o quadrado deste número.

OBS: Em funções Python, os parâmetros com valores default devem sempre estar ao final da declaração
"""
print('----Exemplo 1----')


def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2
print(exponencial(3, 2))  # 3 * 3 * 3

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potência informada pelo usuário
print(exponencial())

print('----Exemplo 2----')


def soma(a=2, b=8):
    return a + b


print(soma(2, 5))
print(soma())

print('----Exemplo 3----')


def mostra_info(nome='Pedro', instrutor=False):
    if nome == 'Pedro' and instrutor:
        return 'Bem-vindo intrutor Pedro'
    elif nome == 'Pedro':
        return 'Não é instrutor'
    return f'Olá {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('Arthur'))

print('----Exemplo 4----')
pessoa = 'Arthur'  # Variável global, se puder evite


def diz_oi():
    pessoa = 'Arthur Antunes'  # Variável local com mesmo nome que global tem preferência
    return f'Oi {pessoa}'


print(diz_oi())

print('----Exemplo 5----')
print('--Função declarada dentro de outra--')


def fora():
    count = 0

    def dentro():
        nonlocal count
        count = count + 1
        return count
    return dentro()


print(fora())
print(fora())
print(fora())
