"""
Geradores

Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterador é um generator.

- Podem ser criados com funções geradoras;
- Funções geradoras usam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras;

Diferenças entre funções e generator functions:

- Função -> Utilizam return;
         -> Retorna uma vez
         -> Quando executada, retorna um valor;

- Generator Function -> Utilizam yield;
                     -> Podem usar yield várias vezes;
                     -> Quando executada, retorna um generator;
"""

print('---- Exemplo de Generator Function----')


def conta_ate(valor_max):
    count = 1
    while count <= valor_max:
        yield count
        count = count + 1


gen = conta_ate(5)
print(type(gen))
print(gen)

for num in gen:
    print(num)
