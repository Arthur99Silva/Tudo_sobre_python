"""
O módulo random

Módulos são outros arquivos Python.

Módulo random -> Possui várias funções para geração de números pseudo-aleatório.

random() -> Gera um número pseudo-aleatório entre 0 e 1;

uniform() -> Gerar um número pseudo-aleatório entre os valores estabelecidos;

randint() -> Gera um número pseudo-aleatório entre os valores estabelecidos inteiros;

choice() -> Mostra um valor aleatório iterável;

shuffle() -> Embaralha dados;
"""
# Existem duas formas de se utilizar um módulo ou função

print('----Forma 1 - Importando todo o módulo----')  # Não recomendado
import random

print(random.random())

print('----Forma 2 - Importando uma função específica do módulo----')  # Recomendada
from random import random

for i in range(10):
    print(random())

print('----Função uniform()----')
from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

print('----Função randint()----')
from random import randint

for i in range(5):
    print(randint(0, 100))

print('----Função choice()----')
from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']
print(choice(jogadas))

print('----Função shuffle()----')
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
