"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""
print('----Exemplo 1----')
num = {num for num in range(0, 7 )}
print(num)

print('----Exemplo 2----')
numeros = {x ** 2 for x in range(10)}
print(numeros)
