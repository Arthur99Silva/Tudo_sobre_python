"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

dunder repr -> Representação do objeto
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
"""


class Livro:
    def __init__(self, titulo, autor, pag):
        self.titulo = titulo
        self.autor = autor
        self.pag = pag

    def __str__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.pag

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória!')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Potter Harry', 'Arthur', 400)
livro2 = Livro('Guia IA', 'Jamal',500)

print(livro1)
print(livro2)
print(len(livro1))
print(livro1 + livro2)
print(livro1 * 3)
