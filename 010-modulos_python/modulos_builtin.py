"""
Módulos built-in (módulos integrados que já vem instalados no Python)
_________________________
/Python/Módulos builtin/
------------------------
Para ver todos os módulos disponíveis instalados no Python, visite:
https://docs.python.org/3/py-modindex.html

# Utilizando alias ou apelidos para módulos/funções
import random as rdm
print(round(rdm.random(), 3))



# Podemos importar todas as funções de um módulo utilizando o *

# import tudo que está no módulo random
from random import *
print(random())

# No importe o módulo random (import random), se quisermos usar qualquer método contido nesse módulo
# precisamos usar random.nome_da_funcao

import random
print(random.random())

# usando um alias para função
from random import randint as rdi, random as rdm
[print(rdi(1, 6)) for _ in range(3)]
[print(rdm()) for _ in range(3)]
"""

# Costumamos utilizar tuples para fazer multiplos imports de um mesmo módulo
# sendo um por linha FORMA PYTHONICA para multiplos imports
from random import (
    random,
    shuffle,
    randint,
    choice)
print(random())

lista = ['a', 'b', 'c']
print(lista)
shuffle(lista)
print(lista)

print(randint(1, 5))

print(choice('Geek University'))
