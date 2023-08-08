"""
Dunder Main e Dunder Name

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando Double Under para não
gerar conflito com os nomes desses elementos na programação.

Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá á variável
__name__ o valor __main__ indicando que este módulo é o de execução principal.
"""
from funcoes_com_parametros import soma

print('----Exemplo Dunder----')

print(soma(12, 6))
