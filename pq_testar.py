"""
Por que testar nosso código?

- Reduzir bugs (problemas) no código existe;
- Testes garantem que novos recursos da sua apticaçào nSo quebren (alterem) recurso antigos;
- Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
- Testes garantem que a refatoraçáo que costuamos a fazer não tragam novos bugs;

Testes automatizados

TDD - Test Driven Devetopment (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
- Você escreve seu teste primeiro;
- Então você escreve 0 código suficiente para fazer 0 teste passar (ou seja, executar com sucesso);
- Então refatora o código para realizar a funcionalidade e testa novamente;
- Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD sào quase como um mantra que os desenvolvedores seguem, conhecidos como:
- Red;
- Green;
- Refactor;


"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} esta miando...')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
