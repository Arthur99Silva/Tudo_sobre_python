"""
Debugando código com PDB

PDB -> Python Debugger

Para utilizar o debbuger é preciso importar a biblioteca import pdb e usar a função set_trace()

Comandos PDB:

- l: listar onde estamos no código
- n: próxima linha
- p: imprime variável
- c: continua/finaliza a execução

print('----Exemplo 1----')


def dividir(a, b):
    # A utilização do print para debugar é uma prática ruim
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto:{err}'


print(dividir(4, 7))

"""
print('----Exemplo 2----')


# Usando o PDB
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Valor incorreto:{err}'


print(dividir(4, 7))

print('----Exemplo 3----')
import pdb
nome = 'Arthur'
sobrenome = 'Antunes'
pdb.set_trace() # = breakpoint()
completo = nome + ' ' + sobrenome
pessoa = 'Jamal'
final = completo + 'é o' + pessoa
print(final)

