"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance.
"""
from _collections import deque

deq = deque('Arthur')
print(deq)

# Adicionando elementos no Deque

deq.append('y')
print(deq)

deq.appendleft('x')
print(deq)

# Remover elementos
print(deq.pop()) # Remove e teorna o ultimo elemento
print(deq)

print(deq.popleft())
print(deq)
