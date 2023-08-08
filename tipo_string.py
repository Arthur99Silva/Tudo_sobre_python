"""
Tipo String

"""
# Maiscula

nome = "Arthur Antunes"

print(nome.upper())

# Minuscula

print(nome.lower())

# Separar e colocar em uma lista de strings

print(nome.split())

# Acessar os caracteres na lista de strings
# ['a', 'r', 't', 'h', 'u', 'r'] -> [0, 1, 2, 3, 4, 5]

print(nome[0:4]) # Slice de string

print(nome[5:9]) # Slice de string

# [0 , 1] -> ['Arthur', 'Antunes']
print(nome.split()[0])

# Inverter a string

print(nome[::-1])

# Substituir um caractere

print(nome.replace('A', 'D'))