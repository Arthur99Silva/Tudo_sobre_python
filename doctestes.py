"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

python -m doctestes -v doctestes.py

"""


def soma(a, b):
    """soma os numewros a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b


# print(soma)

# Outro exemplo

def duplicar(valores):
    """Duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]
