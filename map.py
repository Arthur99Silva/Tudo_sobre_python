"""
Map

Com map, fazemos mapeamento de valores para função.

Map é uma função que recebe dois parâmetros:
1 - Função;
2 - Um iteravél
E retorna um map object
"""
import math
print('----Exemplo 1----')


def area(r):
    """Calcula a área de um círculo com raio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]


print('--------------------------')
print('Forma comum')
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)
print('--------------------------')

print('Forma utilizando map')
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
print('--------------------------')

print('Forma de map com lambda')
print(list(map(lambda r: math.pi * ( r ** 2), raios)))

print('----Exemplo 2----')
cidades = [('Berlin', 29), ('Cairo', 32), ('Los Angeles', 30), ('Rio de Janeiro', 28), ('Tokio', 23)]

print(cidades)
#f = 9/5 * c + 32 Celcius para Farenheit
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
