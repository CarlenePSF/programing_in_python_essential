"""
Pacotes

Diferença entre módulos e pacotes

Modulo -> É simplesmente um ARQUIVO (script) Python que pode ter diversas funções para utilização

Pacotes -> É um DIRETÓRIO contendo uma coleção de módulos

OBS: Nas versões 2.x do Python, um pacote deveria conter um arquivo __init__.py
     Nas versões 3.x do Python, a utilização desse arquivo não é mais obrigatória. Porém ele ainda é
     utilizado para manter compatibilidade reconhecendo quando um diretório é um pacote.


# ----- Exemplo 1 ------

# acessando pacotes
from geek import geek1, geek2

# acessando sub-pacotes
from geek.university import geek3, geek4


print(geek1.pi)
print(geek1.funcao1(1, 2))

print(geek2.curso)
print(geek2.funcao2('Geek University'))

print(geek3.funcao3())
print(geek4.funcao4())
print(geek2.funcao2(geek3.funcao3() + ' ' + geek4.funcao4()))


"""


# ----- Exemplo 2 ------
# Acessando uma função específica

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4


print(funcao1(2, 6))
print(funcao4())
