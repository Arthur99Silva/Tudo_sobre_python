"""
Sistema de Arquivos - Navegação

Para fazer o sudo de manipulção de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

getcwd() -> Pega o diretório de trabalho corrente. Retorna o path absoluto;

os.chdir('...') -> Muda o diretório;

os.path.isabs('...') -> Chega se um diretório é absoluto;

os.name -> Mostra qual o sistema operacional;

os.uname() -> Mostra mais detalhes do sistema operacional;

sys.platform -> Mostra a plataforma;

os.path.join() -> Rcebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o que será juntado ao atual;

os.listdir() -> Lista os diretórios;

os.scandir() -> Lista os arquivos e diretórios com mais detalhes;

scanner.close() -> Usado para fechar a função scandir();

"""
import os
import sys

print(os.getcwd())

print(os.path.isabs('/Users/arthu/'))

print(os.name)

print(sys.platform)
