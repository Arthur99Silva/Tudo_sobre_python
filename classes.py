"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:

- Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos
representar computacionalmente os estados de um objeto. Ao caso da lâmpada, possivelmente
iriamos querer saber se a lampada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou
outra cor, qual é a luminosidade dela e etc.

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este
objeto pode realizar no seu sistema. No caso da Iàmpada, por exemplo, um comportamento comum
que muito provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar
a mesma.

Em Python, para definir uma classe uti lizamos a palavra reservada class.
OBS: Utiizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.
"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))
