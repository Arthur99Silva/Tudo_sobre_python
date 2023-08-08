"""
Reduce

Para entender a função reduce():

- Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, ..., an]

- E você tem uma função que recebe dois parâmetros:
def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe 2 parâmetros, a função e o iterável: reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:

Passo 1 - res1 = f(a1, a2) -> Aplica a função nos dois primeiros elementos da coleção e guarda o resultado

Passo 2 - res2 = f(res1, a3) -> Aplica a função passando o resultado do passo 1 mais o terceiro elemento da e guarda o
                                resuldado

Isso se repete até o final.

Passo 3 - res3 = f(res2, a4)
 .
 .
 .
 Passo n - resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), ...), an)))
"""
# Vamos usar o reduce() para multiplicar todos os números de uma lista
print('----Exemplo 1----')
print('-Usando reduce-')
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

print('-Utilizando um loop normal-')
res = 1
for n in dados:
    res = res * n

print(res)
