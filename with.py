"""
Bloco With

Passos para trabalhar com um arquivo:

1 - Abre o arquivo;
2 - Manipular o arquivo;
3 - Fecha o arquivo;

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilzados são fechados após o with.
"""
with open('texto.txt') as arquivo:
    print(arquivo.readlines())

