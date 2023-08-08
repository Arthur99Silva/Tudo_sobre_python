"""
Sistema de Arquivos - Manipulação

os.mkdir() -> Cria um diretório, caso exista apresenta o erro FileExistsError;

os.makedirs() -> Cria multi-diretórios(árvore de diretórios);

os.rename() -> Renomear diretórios e arquivos;

os.remove() -> Remover arquivos;

os.rmdir() -> Remover diretórios;

os.removedirs() -> Remover uma árvore de diretórios vazios;

send2trash() -> Vai para a lixeira(from send2trash import send2trash)

Removendo uma árvore de diretórios
for arquivo in os.scandir('Diretório'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)

# Outro exemplo
for arquivo in os.scandir('Diretório'):
    print(f'-{arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

--> sudo apt-get install lsb-core
"""
import os
import tempfile

print('----Descobrindo se um arquivo existe----')
print(os.path.exists('novo.txt'))  # Se existir = True
print(os.path.exists('arquivo.txt'))  # Se não existir = False

print('----Descobrindo se um diretório existe----')
print(os.path.exists('curso/pacote_curso'))  # Se existir = True
print(os.path.exists('geek'))  # Se não existir = False

print('----Criando arquivos----')

print('--Forma 1--')
open('arq-teste.txt', 'w').close()

print('--Forma 2--')
open('arq-teste2.txt', 'a').close()

print('--Forma 3--')
with open('arq-teste3.txt', 'w') as arquivo:
    pass

print('--Forma 4 - Mais correta porém windows não suporta mknod--')
#os.mknod('arq-teste4.txt')

print('----Trabalhando com arquivos e diretórios temporários----')
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arq_temp.txt'), 'w') as arquivo:
        arquivo.write('Arthur\n')
    input()

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Arthur Antunes\n')
    tmp.seek(0)
    print(tmp.read())
