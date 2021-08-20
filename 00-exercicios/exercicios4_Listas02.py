"""
Exercícios 02 sobre listas, tuplas, dicionário, sets
"""
# from random import seed
# import random
import numpy as np


# from math import sqrt
# seed random number generator
# np.random.seed()
# seed(25)

# Gerando uma matriz aleatória (lista aninhada) para usar nos exercícios


def gera_matrix(n, tipo=None):
    """
    Gera uma matriz quadrada de dim n com entradas aleatórias
    parameters:
        n:
        tipo: Nome(default), zero
    returns:
        a n dimensional quadratic matrix
    """
    if tipo == 'zero':
        return [[0 for _ in range(n)] for _ in range(n)]
    else:
        return [[np.random.randint(0, 100) for _ in range(n)] for _ in range(n)]


def identity(n):
    """
    Gera uma matrix identidade.
    parameters:
        n: integer
                dimension of the matrix.
    """
    m_id = gera_matrix(n)
    for i in range(n):
        for j in range(n):
            if j == i:
                m_id[i][j] = 1
            else:
                m_id[i][j] = 0
    return m_id


DIM = 4
matrix = gera_matrix(DIM)
for m1 in range(DIM):
    print(matrix[m1])

# ---------------------------------------------------------
# Exercício 1 - elementos de uma matrix 5x5 maiores que 10
# ---------------------------------------------------------
"""
count = 0
maior_dez = []
for _ in range(len(matrix)):
    for _ in range(len(matrix)):
        if matrix[_][_] > 10:
            count += 1
            maior_dez.append(matrix[_][_])


print(f'A matriz contem {count} elementos maiores que 10 que são {set(maior_dez)}')
"""

# ----------------------------------------------------
# Exercício 2 - matriz identidade 5x5
# ----------------------------------------------------
"""
identidade = identity(5)
print(identidade)
"""

# --------------------------------------------------------
# Exercício 3 - outra matriz 5x5 com entradas que são o i*j
# --------------------------------------------------------
"""
matrix_3 = gera_matrix(4)
# print(matrix_3)
for linha in range(len(matrix_3)):
    for coluna in range(len(matrix_3)):
        matrix_3[linha][coluna] = linha * coluna
print(matrix_3)
"""

# ---------------------------------------------------------
# Exercício 4 - posição do maior elemento de uma matrix 5x5
# ---------------------------------------------------------

maiores = []
for _ in range(len(matrix)):
    maiores.append(max(matrix[_]))
print('\n')
print(maiores)
linha = 0
coluna = 0

for m1 in range(DIM):
    for m2 in range(DIM):
        if matrix[m1][m2] == max(maiores):
            linha = m1
            coluna = m2
print(f'O maior elemento da matrix é {max(maiores)} e está localizado na linha {linha + 1} e coluna {coluna + 1}')
