"""
Teste de Memória com Generators

Fibonaccci = 1, 1, 2, 3, 5, 8, 13...
"""
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(100):
    print(n)
