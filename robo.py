class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

        @property
        def nome(self):
            return self.__nome

        @property
        def bateria(self):
            return self.__bateria

        @property
        def habilidades(self):
            return self.__habiladades

        def carregar(self):
            self.__bateria = 100

        def dizer_nome(self):
            if self.__bateria > 0:
                self.__bateria -= 1
                return f'BEEEEP. Eu sou o {self.__nome.upper()}'
            return 'Bateria fraca, recarregue'

        def aprender_habilade(self, nova_habilidade, custo):
            if self.__bateria >= custo:
                self.__bateria -= custo
                self.__habilade.append(nova_habilidade)
                return f'Aprendi {self.__nova_habildade.upper()}'
            return 'Bateria insuficiente!'
