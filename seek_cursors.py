"""
Seek e Cursors

seek() -> É usada para movimentar o cursor pelo arquivo. Ela recebe uma parâmetro que indica onde
          o cursor será colocado.

readline() -> Função que lê o arquivo linha por linha

readlines() -> Função que lê as linhas do arquivo

close() -> Fecha o arquivo


"""
arquivo = open('texto.txt')

#print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
#arquivo.seek(0) # O [0] é a posição que o cursor será colocado
#print(arquivo.read())

#ret = arquivo.readline()
#print(ret)

linhas = arquivo.readlines()

print(len(linhas))

arquivo.close()
