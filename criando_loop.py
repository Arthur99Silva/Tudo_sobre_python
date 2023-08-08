"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Arthur':
    print(letra)

iter([1, 2, 3, 4, 5])
iter('Arthur')
"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Arthur')