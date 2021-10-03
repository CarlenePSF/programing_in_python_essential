"""
Exercícios 02 - listas, tuples, dicionário, sets

OBS: Como essa lista tem mais exercícios de matrizes - listas aninhadas em python- vamos utilizar a biblioteca
numpy, específica para trabalhar com arrays multidimensionais

"""
# import matplotlib.pyplot as plt
# from random import seed
# import random
# from collections import Counter
# from random import sample
from random import seed
import numpy as np
# import pandas as pd
# from math import sqrt
# seed random number generator
np.random.seed(25)
seed(25)

DIM = 4

# Gerando uma matriz aleatória (lista aninhada) para usar nos exercícios


def gera_matrix(n, tipo=None):
    """
    Gera uma matriz quadrada de dim n com entradas aleatórias
    parameters:
        n:
        tipo: Nome(default), zero - todos os elementos são nulos
    returns:
        a n dimensional quadratic matrix
    """
    if tipo == 'zero':
        return np.zeros((n, n), dtype='int')
        # return [[0 for _ in range(n)] for _ in range(n)]
    else:
        return np.random.randint(0, 100, size=(n, n))
        # return [[np.random.randint(0, 100) for _ in range(n)] for _ in range(n)]


def identity(n):
    """
    Gera uma matrix identidade.
    parameters:
        n: integer
                dimension of the matrix.
    """
    # m_id = gera_matrix(n)
    # for i in range(n):
    #     for j in range(n):
    #         if j == i:
    #             m_id[i][j] = 1
    #         else:
    #             m_id[i][j] = 0
    # return m_id
    return np.identity(n)


# zero = gera_matrix(DIM, 'zero')
# print(zero)
# identidade = identity(DIM)
# print(identidade)


# Para os exercícios de 1 a 5 uncomment the lines below
# matrix = gera_matrix(DIM)
# print(matrix)

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
"""
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
"""

# ---------------------------------------------------------
# Exercício 5 -
# ---------------------------------------------------------
"""
valor = int(input('Digite um número: '))
linha = 0
coluna = 0

for m1 in range(DIM):
    for m2 in range(DIM):
        if matrix[m1][m2] == valor:
            linha = m1
            coluna = m2
if linha != 0 and coluna != 0:
    print('Elemento encontrado!')
    print(f'O número inserido está localizado na linha {linha + 1} e coluna {coluna + 1}.')
else:
    print('Valor não encontrado.')
"""

# -----------------------------------------------------------------
# Exercício 6 - Gerar duas matrizes 4x4 e escrever uma terceira com
# os maiores valores de cada posição das matrizes
# -----------------------------------------------------------------
"""
A = gera_matrix(DIM)
print(A)
B = gera_matrix(DIM)
print(B)
C = gera_matrix(DIM, 'zero')

for m1 in range(DIM):
    for m2 in range(DIM):
        if A[m1][m2] > B[m1][m2]:
            # print(A[m1][m2])
            C[m1][m2] = A[m1][m2]
        else:
            # print(B[m1][m2])
            C[m1][m2] = B[m1][m2]
print(C)
"""

# -----------------------------------------------------------
# Exercício 7 - Gerar uma matriz quadrada,
# onde os elementos são da seguinte forma
# A[i][j] = 2i+7j-2, se i<j
# A[i][j] = 3i**2-1, se i=j
# A[i][j] = 4i**3-5j**2+1, se i>j
# -----------------------------------------------------------
""""
def matriz(n):
    m = gera_matrix(n, 'zero')
    for m1 in range(n):
        for m2 in range(n):
            if m1 < m2:
                m[m1][m2] = 2*m1+7*m2-2
            elif m1 == m2:
                m[m1][m2] = 3*m1**2-1
            elif m1 > m2:
                m[m1][m2] = 4*m1**3-5*m2**2+1
    return m


print(matriz(3))
"""
# ----------------------------------------------------------------
# Exercício - Calcular a soma dos elementos que estão:
# (8) acima da diagonal principal;
# (9) abaixo  da diagonal principal;
# (10) na diagonal principal;
# (11) diagonal secundária.
# ----------------------------------------------------------------
"""

m = gera_matrix(DIM)
print(m)
print('\n')

principal = []
acima = []
abaixo = []
secundaria = []
for m1 in range(DIM):
    for m2 in range(DIM):
        if m1 < m2:
            acima.append(m[m1][m2])
        elif m1 > m2:
            abaixo.append(m[m1][m2])
        elif m1 == m2:
            principal.append(m[m1][m2])
        if m2 == DIM - 1 - m1:
            secundaria.append(m[m1][m2])


print(f'Os elementos acima da diagonal principal são {acima}.', f'Sua soma é {sum(acima)}')
print(f'Os elementos da diagonal principal são {principal}', f'A sua soma é {sum(principal)}')
print(f'Os elementos abaixo da diagonal principal são {abaixo}.', f'A soma deles é {sum(abaixo)}')
print(f'Os elementos da diagonal secundária  são {secundaria}.', f'A soma deles é {sum(secundaria)}')
"""

# --------------------------------------------------------------------
# Exercício 12 - Transpondo uma matriz
# --------------------------------------------------------------------
"""
matrix = gera_matrix(3)
print(matrix.shape)
print(matrix)
matrix = matrix.transpose()
print(matrix)
"""


# --------------------------------------------------------------------
# Exercício 13 - Matriz triangular inferior
# --------------------------------------------------------------------
'''
def triangular_inferior(n):
    """
    Transforma uma matriz de dim nxn cujas entradas são numeros no intervalo de 1-20
    numa triangular inferior.
    """
    m = np.random.randint(1, 20, size=(n, n))
    print(m)
    for m1 in range(n):
        for m2 in range(n):
            if m1 < m2:
                m[m1][m2] = 0
    return m


print(triangular_inferior(4))
'''

# --------------------------------------------------------------------
# Exercício 14- uma cartela de bingo
# --------------------------------------------------------------------
"""
# verificando se os elementos sorteados não se repetem


def frequency_table(conjunto):
    unique, counts = np.unique(conjunto, return_counts=True)
    data = {'elementos': unique, 'frequencia': counts}
    return pd.DataFrame.from_dict(data, orient='columns')


cartela = []

sorteados = sample(range(0, 99), 25)
print(sorteados)
print(frequency_table(sorteados))

# construindo a cartela
for i in range(5):
    cartela.append(sorteados[i*5:5*i+5])
print(cartela)
"""

# --------------------------------------------------------------------
# Exercício 15- Construtor de gabarito
# --------------------------------------------------------------------

numero_questoes = 10
numero_alunos = 5


def respostas_alunos(num_questions, num_alunos):
    respostas = []
    for _ in range(num_alunos):
        res = [input(f'digite as respostas da questão {_+1}: ') for _ in range(num_questions)]
        respostas.append((f'aluno {_ + 1}', res))
    return respostas


def gabarito(num_questions):
    return 'Gabarito', [input(f'Digite o gabarito da questão {_+1}: ') for _ in range(num_questions)]


Gabarito = gabarito(numero_questoes)
print('\n')
Respostas = respostas_alunos(numero_questoes, numero_alunos)


pontuacao = []
for i in range(numero_alunos):
    pontos = 0
    for j in range(numero_questoes):
        if Respostas[i][1][j] == Gabarito[1][j]:
            pontos += 1
        else:
            continue
    pontuacao.append(f'O aluno {i+1} fez {pontos} pontos')

for i in range(numero_alunos):
    print(f'{pontuacao[i]}.')
