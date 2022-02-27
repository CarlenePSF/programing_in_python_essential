"""
POO — Métodos Mágicos

Métodos mágicos são todos os métodos que utilizam dunder- double ‘underscore’.

1) dunder init → __init__()

2) dunder repr → representação do objeto __repr__()
   dunder str → outra maneira de representar o objeto __str__()

3) dunder len → retorna o tamanho __len__()

4) dunder add → adiciona objeto __add__()

No exemplo abaixo, executamos exemplos de polimorfismo nos métodos da classe object,
pois todas as classes criadas herdarão os métodos de object

"""


class Livro(object):
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __repr__(self):
        return f'{self.titulo}, autor {self.autor}'

    def __str__(self):  # similar o repr
        return self.titulo

    def __len__(self):
        return self.num_paginas

    def __add__(self, other):
        return f'{self} and {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'não posso multiplicar'

    def __del__(self):  # apagando um objeto da memória
        print('O objeto do tipo livro foi deletado da memória.')


livro1 = Livro('Código limpo: Habilidades práticas do Agile Software', 'Robert C. Martin', 425)
livro2 = Livro('Contos de terror, de mistério e de morte', ' Edgar Allan Poe', 240)

print(livro1)  # devolve a representação do objeto no endereço de memória
print(livro2)

print(len(livro1))
print(len(livro2))
print(livro1 + livro2)
print(livro2 * 3)
