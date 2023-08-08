"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada assim como o def ou qualquer outra no Python.

Para simplificar, pense no raise como sendo útil para que podemos criar nossas próprias exceções e mensagens de erro. O
raise finaliza a função assim que o erro for encontrado.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

"""
print('----Exemplo 1----')


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Arthur', 'azul')
colore('True', 'verde')
#colore('Teste', 2)  # Erro está aqui

print('----Exemplo 2----')


def colore(texto, cor):
    cores = ['verde', 'azul', 'branco', 'preto']
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'preto')
#colore('Nicole', 'vermelho') # Erro está aqui
