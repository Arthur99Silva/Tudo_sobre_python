"""
Len, Abs, Sum e Round

len() -> Retorna o tamanho, ou seja, o número de itens de um iterável

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

sum() -> Recebe como parâmetro um iterável, podendo recebr um valor inicial, e retorna a soma total dos elementos,
         incluindo o valor inicial.

round() -> Retorna um número arrendondado para n dígito de precisão após a casa decimal. Se a precisão não for
           informada retorna o inteiro mais próximo da entrada.
"""
print('----Exemplo len()----')
print(len('ARTHUR ANTUNES'))
print(len([1, 2, 3, 4, 5]))
# E por aí vai...

print('----Exemplo abs()----')
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

print('----Exemplo sum()----')
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print('----Exemplo round()----')
print(round(10.2))
print(round(10.5))
print(round(10.8))
print(round(1.21212121, 2)) # Casas decimais
