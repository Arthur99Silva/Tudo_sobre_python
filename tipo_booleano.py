"""
Tipo Booleano

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:
true, false

Certo:
True, False
"""

ativo = True

print(ativo)

logado = False

"""
Operações básicas:
"""

# Negação(not)
# Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
# se for falso o resultado será verdadeiro. Ou seja será sempre o contrário.

print(not ativo)

# Ou(or)
# É uma operação binária, ou seja depende de 2 valores. Ou um ou outro deve ser verdadeira.
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

print(ativo or logado)

# E(and)
# Também é uma operação binária, ou seja depende de dois valores. Ambos valores devem ser verdadeiros.
# True or True -> True
# True or False -> False
# False or True -> False
# False or False -> True

