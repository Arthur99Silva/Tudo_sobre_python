"""
Mapas

Conhecidos em Python como dicionários.
"""
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
print(receita.keys())
print(receita.values())
print('----------------')
# Iterar sobre dicionários
for chave in receita:
    print(chave)
print('----------------')

for chave in receita:
    print(receita[chave])
print('----------------')

for chave in receita:
    print(f'{chave} : {receita[chave]}')
print('----------------')

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
print('----------------')

# Soma*, Valor máximo e mínimo, e Tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
