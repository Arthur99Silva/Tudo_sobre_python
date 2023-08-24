"""
Poo -> Objetos

Objetos -> São instâncias da classe. Ou seja, apôs o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
nos objetos/ instâncias de uma classe como variáveis do tipo definido na classe.


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desl(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


# Instância/Objetos
lamp1 = Lampada('Branca', 110, 60)
lamp1.ligar_desl()
print(f'A lâmpada esta ligada? {lamp1.checa_lampada()}')
