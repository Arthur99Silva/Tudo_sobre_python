"""
Leitura de arquivos

Para ler o conteúdo de um arquivo, utilizamos a função integrada open().

open() -> A forma mais simples de utilização nó passamos apenas um parâmetro de entrada, sendo o nome do arquivo. Essa
função retorna um _io.TestIOWrapper e é com ele que trabalhamos então.

OBS.: Por padrão ao open() abre o arquivo para leitura. Este arquivo deve existir, ou senão apresentará o erro
FileNotFoundError.

A string, define which mode you want to open the file in:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""
print('----Exemplo 1----')
arquivo = open('texto.txt')

#print(arquivo)
#print(type(arquivo))

# Para ler o conteúdo do arquivo, após sua abertura, devemos utilizar read()

print(arquivo.read())

