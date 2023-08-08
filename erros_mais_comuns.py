"""
Erros mais comuns

1 - SyntaxError: Quando existe um erro de sintaxe. Ou seja, foi escrito algo que o Python não reconheceu;
Ex.:
def funcao:
    print('Erro pq faltou o parenteses na decalração')

2 - NameError: Quando uma variável ou função não foi definida;
Ex.:
print(geek)

3 - TypeError: Ocorre quando uma função/operação/ação é aplicada a um tipo errado;
Ex.:
print(len(5))

4 - IndexError: Quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado usando um
                índice inválido;
Ex.: lista ['Arthur']
     print(lista[0])

5 - ValueError: Ocorre quando uma função/operação built-in recebe um argumento de tipo correto mas valor inapropriado;
Ex.: print(int('Arthur'))

6 - KeyError: Quando tenta acessar um dicionário com uma chave que não existe;
Ex.: dic = {'Arthur': 'Antunes'}
     print(dic['Arthur'])

7 - AttributeError: Quando uma variável não tem atributo/função;
Ex.: tupla = (1, 2, 3)
     print(tupla.sort())

8 - IndentationError: Erro de indetação do código;
"""