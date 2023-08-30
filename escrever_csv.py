"""
Escrevendo em arquivos CSV

reader() (tei toro, writer() (escritor)

writerow() -> Escreve uma linha


"""
# wrlter() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.


from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor = writer(arquivo)
    filme = None
    escritor.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Nome do filme:')
        if filme != 'sair':
            genero = input('Gênero:')
            duracao = input('Duração:')
            escritor.writerow([filme, genero, duracao])