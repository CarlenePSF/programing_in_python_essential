 """

Listas aninhadas (Nested lists)

-Algumas linguagens de programacao como C/Java/PHP  possuem uma estrutura de dados conhecida como arrays:
    - Unidimensionais (array/vetores)
    - Multidimensionais (matrizes)


Em  python existe as listas
numeros = [1, 2, 3, 4, 5, 'b', True, 2.41]

# Exemplos
# Como escreveriamos uma matrix 3x3
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)
print(type(listas))


# Como podemos acessar os dados? (indexacao)
# listas [linha][coluna]

print(listas[0][0])   # acessando o elemento 1
print(listas[2][1])   # acessando o elemento 8


# Como iterar com loops numa lista aninhada?

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in listas:
    for num in i:
        print(num)


# Como usar o list comprehension com listas aninhadas?
# Seguindo o exemplo do loop anterior


listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(num) for num in i] for i in listas]

# Gerando um tabuleiro 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)


# Incluindo jogadas num jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])

OBS: list comprehension talvez sacrifique a clareza do codigo em detrimento da reducao do numero de linhas
"""
from random import randint, seed
seed()

# Somando duas matrizes
# noinspection PyRedeclaration
v = [[randint(1, 10) for i in range(0, 3)],
     [randint(1, 10) for i in range(0, 3)],
     [randint(1, 10) for i in range(0, 3)]]

u = [[i for i in range(1, 4)],
     [i for i in range(4, 7)],
     [i for i in range(7, 10)]]

print(v)
print(u)

[[print(v[j][i]+u[j][i]) for i in range(0, 3)] for j in range(0, 3)]
