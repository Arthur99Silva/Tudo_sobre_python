"""
Definindo funções

- Funções são pequenos trechos de código que realizam tarefas especifícas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

Já utilizamos várias funções: print(), len(), max(), min(), etc;

Em Python a forma geral de definir uma função é:
def nome_da_funcao(parametros_entrada):
    bloco_funcao

OBS: 1 - Veja que dentro das nossas funções podemos usar outras funções;
     2 - Veja que nossa função(diz_oi) executa apenas uma tarefa;

"""
# Exemplo de utilização de funções
cores = ['verde', 'vermelho', 'amarelo', 'azul']

# Utilizando a função integrada no Python
print(cores)
print('-------------')

nome = 'arthur'
print(nome)

cores.append('roxo')
print('-------------')
print(cores)
print('-------------')

print('----Definindo a primeira função----')


def diz_oi():
    print('Oi!')


# Utilizando a função
diz_oi()
print('-------------')


# Exemplo 2
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('...')


#for n in range(5):
#    cantar_parabens()

# Podemos criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens

canta()
