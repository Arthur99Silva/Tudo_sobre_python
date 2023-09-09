"""
Assertions (afirmações)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressáo que queremos checar se é válida ou nâo.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada;

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso.... não precisa ser exclusivamente
nos testes;

Se um programa Python or executa o com o parametro -O, nen um assertion
será validado. Ou seja, todas as suas validações já eram.

"""


def soma_num_pos(a, b):
    assert a > 0 and b > 0, 'Ambos devem ser positivos'
    return a + b


ret = soma_num_pos(2, 4)
#ret2 = soma_num_pos(-2, 4)
print(ret)
print('-------------------------')


def fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'burguer',
        'hotdog'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Qual é a comida:')
print(fast_food(comida))

