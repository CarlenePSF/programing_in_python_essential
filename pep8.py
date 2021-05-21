"""
###################################################################
Pep8 - python enhancement proposal
These are proposals to make the python language better
Zen of python can be accessed by the command  'import this'
###################################################################
the idea is that we can write python codes in a pythonize way

[1] - Use Camel Case for class names (utilizar Camel Case para nomes de classes)

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Use names without capitol latter + underline space to funtions or variables
def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5


[3] - Use 4 spaces to indent you code!!! Do not use tabs

if 'a' in "banana":
    print("tem")

if ('a'=='a'):
    print('true')

[4] - white lines ou Linhas em branco

-- Separar funcoes e definicoes de classe com duas linhas em branco;
-- metodos dentro de uma classe devem ser separados com uma unica linha em branco;

[5] Imports must be tipped in different lines --  imports devem ser feitos em linhas separadas

#  Import errado
import sys, os

# Import certo

import sys
import os

# Nao ha problema em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,

)

# Imports devem ser colocados no topo dos arquivos logo depois de quaisquer comentarios ou docstring
# e antes de constantes ou variaveis globais

[6] - Espacos em expressoes e instrucoes

# Nao faca:

funcao( algo[ 1 ], {outro: 2} )

# Faca:
funcao(algo[1],{outro:2})

# nao faca:

algo (1)

#faca:

algo(1)

# Nao faca
dict ['chave'] = list [indice]

# faca:
dict['chave'] = list[indice]

# Nao faca (para declarar variaveis):

x              = 3
y              = 4
variavel_longa = 5


# Faca (para declarar variaveis):

x = 3
y = 4
variavel_longa = 5


[7] - End an instruction with a new line

"""


import this