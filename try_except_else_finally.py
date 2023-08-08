"""
Try, Except, Else e Finally

Dica de quando e onde tratar código: TODA ENTRADA DEVE SER TRATADA!

A função do usuário é destruir seu sistema.

O finally, geralmente é usado para fechar ou desalocar recursos.
"""
print('----Exemplo 1 - Else----')

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou: {num}')

print('----Exemplo 2 - Finally----')

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou: {num}')
finally:
    print('Executando o finally')

print('----Exemplo 3----')


def dividir(a, b):
    return a / b


num1 = int(input('Digite o valor do primeiro número: '))


try:
    num2 = int(input('Digite o valor do segundo número: '))
except ValueError:
    print('Precisa ser um número')
try:
   print(dividir(num1, num2))
except ValueError:
    print('Valor incorreto')

print('----Exemplo 4----')


def dividir_num(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Não é possível fazer divisão por zero!'


num1 = input('Digite o valor do primeiro número:')
num2 = input('Digite o valor do segundo número: ')

print(dividir_num(num1, num2))
