"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Virgula

A linguagem Python possui duas formas diferente para ler dados em arquivos CSV:

reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
next() -> Pula o cabeçalho

"""

arquivo = open('lutadores.csv', encoding="utf8")
dados = arquivo.read()
#print(type(dados))
dados = dados.split(',')
print(dados)
