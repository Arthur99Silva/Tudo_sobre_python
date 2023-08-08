"""
Decoradores(Decorators)

- São funções que envolvem outras funções e aprimora seu comportamento;
- São exemplos de High Order Functions;
- Tem sintaxe própria, usando "@" (Syntact Sugar);

*------------------*
* Função Decorator *
*------------------*

*---------------------*
*---------------------*
*-- Função decorada --*
*---------------------*
*---------------------*

"""
print('----Exemplo 1 - Decorators como funções----') # Não recomendada sem Syntact Sugar


def seja_educado(funcao): # Isso é uma Função Decorator
    def sendo():
        print('Prazer te conhecer!')
        funcao()
        print('Tenha um bom dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a)!')


teste = seja_educado(saudacao)
teste()

print('----Exemplo 2 - Decorators como funções----')


def raiva():
    print('TE ODEIOOOO!')


raiva_educada = seja_educado(raiva)
raiva_educada()

print('----Exemplo 3 - Com Syntact Sugar ----')


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Grande prazer te conhecer!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo # Isso é um decorator
def apresentando():
    print('Meu nome é Arthur!')


apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()
