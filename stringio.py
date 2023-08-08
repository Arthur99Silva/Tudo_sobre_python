"""
StringIO

Para ler ou escrever dados em arquivos operacional o software precisa ter permissão:
- Permissão de leitura para ler o arquivo;
- Permissão de escrita para escrever no arquivo;

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
from io import StringIO

mensagem = 'String normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserir um texto
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora é utilizar o que foi aprendido
print(arquivo.read())
