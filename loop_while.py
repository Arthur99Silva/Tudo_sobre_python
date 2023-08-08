"""
Loop While

while expressão booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

"""
# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1 # Esse é o critério de parada

#OBS: Em um loop while é importante que cuidemos do critério de parada para não causar um loop infinito.

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')
