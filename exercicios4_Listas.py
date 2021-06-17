"""
Exercicios de listas
"""
from random import seed, randint

# seed random number generator
seed()
import numpy as np


"""
#---------------------------------
# Exercicio 1 - 
#---------------------------------

A = [1, 0, 5, -2, -5, 7]
print(A)
soma = A[0]+A[1]+A[5]
print(f'A soma dos elemento {A[0]}+{A[1]}+{A[5]} é {soma}')

A[4] = 100
for i in range(0, 6):
    print(f'{A[i]}')

#--------------------------------------------
# Exercicio 2 - lendo e imprimindo inteiros
#-------------------------------------------

V = []
for i in range(0, 6):
    n = float(input(f'Entre com o elemento V[{i}]: '))
    V.append(n)
print(V)

#----------------------------------
# Exercicio 3 -
#---------------------------------

v1 = []
v2 = []

for i in range(0, 10):
    a = randint(0, 10)
    v1.append(a)
    v2.append(a**2)
print(v1)
print(v2)

# ****  Opcao usando a biblioteca numpy *****
# A dimensão do vetor deve ser especificada
v1 = np.empty([10,1])
v2 = np.empty([10,1])

for i in range(0, 10):
    a = randint(0, 10)
    v1[i] = a
    v2[i] = a**2
print(v1)
print(v2)

#----------------------------------
# Exercicio 4 -
#---------------------------------

v = []
for i in range(0, 8):
    a = randint(0, 10)
    v.append(a)
print(f'Seja o vetor {v}.')

n1 = int(input("digite um valor inteiro entre 0-7: "))
n2 = int(input("digite outro valor inteiros entre 0-7: "))

print(f'Os valores de v na posicao {n1} e {n2} sao {v[n1]} e {v[n2]}.')
print(f'A soma desses valores e {v[n1]+v[n2]}')

#--------------------------------------------------
# Exercicio 5 - contando elementos pare de um vetor
#--------------------------------------------------
v = []
soma = 0
for i in range(0, 10):
    a = randint(0, 10)
    v.append(a)
    if v[i] % 2 == 0:
        soma = soma+1

print(f'O vetor {v} tem {soma} elementos pares!.')

#--------------------------------------------------
# Exercicio 6 - maior e menor elemento de um vetor
#--------------------------------------------------

v = []
for i in range(0, 10):
    a = randint(0, 10)
    v.append(a)
ordenado = sorted(v)
print(f'O menor elemento de do vetor {v} e {ordenado[0]}')
print(f'O maior elemento do vetor {v} e {ordenado[9]}')
#print(f'O vetor {v} tem {soma} elementos pares!.')


#-----------------------------------------------------------------
# Exercicio 7 - Imprimindo a posicao do maior elemento de um vetor
#-----------------------------------------------------------------

v = []

for i in range(0, 10):
    a = randint(0, 100)
    v.append(a)
ordenado = sorted(v)
print(f'O vetor v gerado: {v}')
print(f'O maior elemento do vetor v: {ordenado[9]}')
for i in range(0, 10):
    if v[i] == ordenado[9]:
        print(f'A posicao do maior elemento {ordenado[9]}: v[{i}]')


#-----------------------------------------------------------------
# Exercicio 8 - Imprimindo vetor na ordem inversa
#-----------------------------------------------------------------

v = []
i = 5
for i in range(0, 6):
    a = randint(0, 100)
    v.append(a)
print(v)
while i >= 0:
    print(v[i])
    i = i-1


#-----------------------------------------------------------------
# Exercicio 9 - Imprimindo vetor de numeros pares na ordem inversa
#-----------------------------------------------------------------

v = []
i = 5
while len(v) <= 5:
    a = randint(0, 100)
    if a % 2 == 0:
        v.append(a)
print(v)
while i >= 0:
    print(v[i])
    i = i-1


#-----------------------------------------------------------------
# Exercicio 10 - media das notas de classe com 15 alunos
#-----------------------------------------------------------------

notas = []
soma = 0
for i in range(0, 15):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma = soma + notas[i]
print(len(notas))
print(f'A média das notas é {soma/len(notas)}')
"""


#-----------------------------------------------------------------
# Exercicio 11 - media das notas de classe
#-----------------------------------------------------------------

negativos = []
positivos = []
qtn_negativo = 0

soma = 0

for i in range(10):
    n = float(input("Digite um número: "))
    if n < 0:
        negativos.append(n)
        qtn_negativo = qtn_negativo + 1
    else:
        positivos.append(n)
        soma = soma + n

print(f'Foram digitados {qtn_negativo} numeros negativos.')
print(f'Os numeros negativos digitados foram {negativos}')
print(f'A soma dos numeros positivos digitados é {soma}')



