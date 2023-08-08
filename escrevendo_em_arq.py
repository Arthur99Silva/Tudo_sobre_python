"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura, não se pode realizar escrita nele. Apenas leitura. Da mesma forma, se abrirmos uma
arquivos para escrita não é possível lê-lo, somente escrever.

Para escrever dados em um arquivo, após abrir o arquivo deve-se utilizar a função write(). Esta função recebe uma
string como parâmetro.

Abrindo o arquivo para escrita 'w', se o arquivo existir a versão anterior será apagada e uma nova será criadq. Dessa
forma todo conteúdo do anterior será perdido.
"""
print('----Exemplo 1 - Escrita----')
with open('novo.txt', 'w') as arquivo: # w = escrita
    arquivo.write('Escrevendo dados nesse arquivo durante o curso Udemy.\n')
    arquivo.write('Linhas ilimitadas para escrever.\n')
    arquivo.write('Última linha do arquivo 123.\n')

with open('novo_2.txt', 'w') as arq:
    arq.write('Arthur\n' * 100)

with open('novo_3.txt', 'w') as arq:
    arq.write('Antunes\n' * 100)

with open('frutas.txt', 'w') as arq2:
    while True:
        fruta = input('Informe uma frutas ou digite sair:')
        if fruta != 'sair':
            arq2.write(fruta + '\n')
        else:
            break
