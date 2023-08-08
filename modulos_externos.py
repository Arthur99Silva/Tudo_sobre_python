"""
Instalando e utilizando módulos externos

Utilizamos o gerenciador de pacote Python chamado pip.

http://pupi.org -> Pcotes oficiais

colorama -> Permite textos coloridos no terminal

import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)


"""

from colorama import init, Fore
init()
print(Fore.MAGENTA + 'Arthur Antunes')
print(Fore.BLUE + 'Arthur Antunes')
print(Fore.RED + 'Arthur Antunes')