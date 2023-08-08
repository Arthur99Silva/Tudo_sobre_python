"""
Dicionários

OBS: Em algumas linguagens de programação os dicionários Python são conhecidos como mapas.

São coleções do tipo chave/valor. Chaves e valores podem ser de qualquer tipo.

São representados por chaves {}.
"""
# Forma 1

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'rus': "Rússia"}
print(paises)
print(type(paises))
print('----------------')

# Forma 2

paises = dict(br='Brasil', eua="Estados Unidos", rus="Rússia")
print(paises)
print(type(paises))
print('----------------')

# Acessando elementos

# Forma 1 -  Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['rus'])
print('----------------')

# Forma 2 - Acessando via get (Recomentado)

print(paises.get('br'))
print(paises.get('py')) # None -> tipo de dado que representa o tipo sem tipo(vazio). É utilizado para criar variáveis
                        # para inicia-la sem tipo e definar o valor depois.
print('----------------')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('py' in paises)
print('Estados Unidos' in paises)

if 'py' in paises:
    paraguai = paises['py']

print('----------------')

# Chaves e valores podem ser de qualquer tipo

localidades = {(35.6895, 39.6917): 'Tokio',
               (40.7128, 74.0060): 'NY',
               (37.7749, 122.4299): 'SP'}
print(localidades)
print(type(localidades))
print('----------------')

# Adicionar elementos no diciomário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))
print('----------------')

# Forma 1
receita['abr'] = 200
print(receita)
print('----------------')

# Forma 2
novo_dado = {'mai': 350}
receita.update(novo_dado)
print(receita)
print('----------------')

# Atualizando dados no dicionário

# Forma 1

receita['mai'] = 550
print(receita)
print('----------------')

# Forma 2

receita.update({'mai': 600})
print(receita)
print('----------------')

# Remover dados de um dicionário
# Forma 1
receita.pop('mar')
print(receita)
print('----------------')

# Forma 2
del receita['jan']
print(receita)
print('----------------')

# Limpar dicionário
#receita.clear()

# Copiar um dicionário para outro
novo = receita.copy()
print(novo)