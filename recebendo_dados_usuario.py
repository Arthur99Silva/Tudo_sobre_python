"""
Recebendo dados do usuário

input() -> Todo dado recebido pelo input é do tipo String

Em Python, é String tudo que estiver entre:

-Aspas simples -> 'Nome'
-Aspas duplas -> "Nome"
-Aspas simples triplas -> '''Nome'''
-Aspas duplas triplas
"""
# Entrada de dados

#print("Qual o seu nome?")
#nome = input() # Input -> entrada
nome = input("Qual o seu nome?")

# Exemplo de print "antigo"
#print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print "moderno"
#print("Seja bem-vindo(a) {0}" .format(nome))

# Exemplo de print atual
print(f"Seja bem-vindo(a) {nome}")

#print("Qual sua idade?")
#idade = input()
idade = int(input("Qual a sua idade?"))

# Processamento

# Saída de dados
#print("A %s tem %s anos" % (nome, idade))
#print("A {0} tem {1} anos" .format(nome, idade))
print(f"A {nome} tem {idade} anos")
"""
int(idade) -> cast  

Cast é a conversão de um tipo de dado para outro
"""
print(f"A {nome} nasceu em {2018 - int(idade)}")
