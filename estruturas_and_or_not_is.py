"""
Estruturas lógicas AND, OR, NOT e IS

Operadores Unários:
    - NOT, IS

Operadores Binários:
    - AND , OR

Para o AND, ambos os valores precisam estar True.
Para o OR, um ou outro valor precisa ser True.
Para o NOT, o valor do booleano é invertido.
Para o IS, o valor é comparado com um segundo
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')

ativa = True

if not ativa:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
else:
    print('Bem-vindo usuário!')

#print(not False)
print(ativa is True)
