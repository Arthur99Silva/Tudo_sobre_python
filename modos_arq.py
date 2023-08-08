"""
Modos de abertura de arquivos

r -> Abre para leitura;
w -> Abre para escrita - sobrescreve caso o arquivo já exista;
x -> Abre para escrita somente se o arquivo não existir;
a -> Abre para escrita, adicionando o conteudo ao final do arquivo;
+ -> Abre para o modo de atualização: Leitura e escrita

"""
with open('frutas.txt', 'a') as arq2:
    while True:
        fruta = input('Informe uma frutas ou digite sair:')
        # noinspection LossyEncoding
        if fruta != 'sair':
            arq2.write(fruta + '\n')
        else:
            break
