"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""

# Refatorando uma função

print('----Exemplo 1----')


def quadrado(numero):
    return numero * numero


print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

ret = quadrado(6)
print(ret)

print('----Exemplo 2----')


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('...')
    print(f'Viva o {aniversariante}!')


cantar_parabens('Arthur')

# Funções podem ter n parâmetros de entrada, ou seja podemos receber como entrada quantos parâmetros forem necessários
print('----Exemplo 3----')


def soma(a, b):
    return a + b


if __name__ == '__main__':
    print(soma(2, 4))
else:
    print('O módulo funcoes_com_parametros foi importado')



print('----Exemplo 4----')


def multiplica(x, y):
    return x * y


print(multiplica(4, 4))


def outra(n, m, msg):
    return (n - m) * msg


print(outra(5, 2, 'Exemplo 3'))

print('----Exemplo 5----')


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}.'


print(nome_completo('Arthur', 'Antunes'))
