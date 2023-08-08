"""
Documentando funções com Docstrings
"""
print('----Exemplo 1----')


def diz_oi():
    """Uma função simples que retorna a string OI!"""
    return 'OI!'


print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)
