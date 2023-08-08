"""
Ranges

- Precisamos conhecer conhecer o loop for para usar os ranges;
- Precisamos conhecer os ranges para trabalhar melhor com loops for;

Ranges são utilizados para gerar sequências númericas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

- Forma 1 -> range(valor_de_parada)
- Forma 2 -> range(valor_inicio, valor_de_parada)
- Forma 3 -> range(valor_inicio, valor_de_parada, passo)
- Forma 4(inversa) -> range(valor_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(início padrão 0, e passo de 1 em 1), passo especificado pelo usuário

"""
# Forma 1
for num in range(11):
    print(num)
print(f'----------------')

# Forma 2
for num in range(1, 11):
    print(num)
print(f'----------------')

# Forma 3
for num in range(1, 10, 2):
    print(num)
print(f'----------------')

# Forma 4
for num in range(10, 0, -1):
    print(num)