"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis Globais;
    -> São reconhecidas , ou seja, seu escopo compreeende todo o programa.

2 - Variáveis Locais;
    -> São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo esta limitado apenas
    ao bloco onde foi declarada.

Para declarar vaeiáveis fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável nós não colocamos o tipo de dado nela.
Esse tipo é inferido ao atribuírmos o valor nela mesma.

Exemplo em C:

int numero = 42;

"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))


numero = 'GEEK'
print(numero)
print(type(numero))


nao_existo = 'oi'
print(nao_existo)

numero = 42
novo = 0

# Novo é uma variável local
if numero > 10:
    novo = numero + 10
    print(novo)

print(novo) # Ela deve ser declarada antes