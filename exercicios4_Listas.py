"""
Exercícios de listas, tuplas, dicionário, sets
"""
# from random import seed
import numpy as np
# seed random number generator
# np.random.seed(25)
np.random.seed(25)

"""
# ---------------------------------
# Exercício 1 - 
# ---------------------------------

A = [1, 0, 5, -2, -5, 7]
print(A)
soma = A[0]+A[1]+A[5]
print(f'A soma dos elemento {A[0]}+{A[1]}+{A[5]} é {soma}')

A[4] = 100
for i in range(0, 6):
    print(f'{A[i]}')

# --------------------------------------------
# Exercício 2 - lendo e imprimindo inteiros
# -------------------------------------------

V = []
for i in range(0, 6):
    n = float(input(f'Entre com o elemento V[{i}]: '))
    V.append(n)
print(V)

# ----------------------------------
# Exercício 3 -
# ---------------------------------

v1 = []
v2 = []

for i in range(0, 10):
    a = randint(0, 10)
    v1.append(a)
    v2.append(a**2)
print(v1)
print(v2)

# ****  Opção usando a biblioteca numpy *****
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
# Exercício 4 -
#---------------------------------

v = []
for i in range(0, 8):
    a = randint(0, 10)
    v.append(a)
print(f'Seja o vetor {v}.')

n1 = int(input("digite um valor inteiro entre 0-7: "))
n2 = int(input("digite outro valor inteiros entre 0-7: "))

print(f'Os valores de v na posição {n1} e {n2} sao {v[n1]} e {v[n2]}.')
print(f'A soma desses valores e {v[n1]+v[n2]}')

#--------------------------------------------------
# Exercício 5 - contando elementos pare de um vetor
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
# Exercício 6 - maior e menor elemento de um vetor
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
# Exercício 7 - Imprimindo a posição do maior elemento de um vetor
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
        print(f'A posição do maior elemento {ordenado[9]}: v[{i}]')


#-----------------------------------------------------------------
# Exercício 8 - Imprimindo vetor na ordem inversa
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
# Exercício 9 - Imprimindo vetor de números pares na ordem inversa
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
# Exercício 10 - media das notas de classe com 15 alunos
#-----------------------------------------------------------------

notas = []
soma = 0
for i in range(0, 15):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma = soma + notas[i]
print(len(notas))
print(f'A média das notas é {soma/len(notas)}')


# -----------------------------------------------------------------
# Exercício 11 - calculando a quantidade de números negativos e a 
# soma dos números positivos de um vetor com 10 entradas
# -----------------------------------------------------------------

negativos = []
positivos = []

for i in range(10):
    n = float(input("Digite um número: "))
    if n < 0:
        negativos.append(n)
    else:
        positivos.append(n)


print(f'Foram digitados um total de {len(negativos)} números negativos.')
print(f'Os números negativos digitados foram {negativos}')
print(f'A soma dos números positivos digitados é {sum(positivos)}')


# -----------------------------------------------------------------
# Exercício 12 - lendo 5 valores e imprimindo o maior e o menor deles
# juntamente com a média aritmética de todos
# -----------------------------------------------------------------
numero = []
for i in range(5):
    entrada = float(input("Digite um número: "))
    numero.append(entrada)

print(f'Os números digitados foram {numero}')
print(f'O maior dentre os números digitados é {max(numero)} e o menor dentre eles é {min(numero)}.')
print(f'A média aritmética desses números é {sum(numero)/5}')


# -----------------------------------------------------------------
# Exercício 13 - lendo 5 valores e imprimindo a posição do
# maior e do menor elemento
# -----------------------------------------------------------------

numero = []
for i in range(5):
    entrada = float(input("Digite um número: "))
    numero.append(entrada)

for i in range(5):
    if numero[i] == max(numero):
        print(f'O maior elemento se encontra na {i+1} posição')
    elif numero[i] == min(numero):
        print(f'O menor elemento está na {i+1} posição')


# -----------------------------------------------------------------
# Exercício 14 - lendo um vetor com 10 posições e verificando se
# existe alguma entrada repetida
# -----------------------------------------------------------------

numeros = []
for i in range(10):
    entrada = float(input("Digite um número: "))
    numeros.append(entrada)

for element in set(numeros):
    qte = numeros.count(element)
    if qte >= 2:
        print(f'Elemento {element} repetido')


# -----------------------------------------------------------------
# Exercício 15 - lendo um vetor com 200 posições e eliminando os
# elementos repetidos
# -----------------------------------------------------------------

numeros = []
for i in range(20):
    entrada = float(input("Digite um número: "))
    numeros.append(entrada)

print(f'{set(numeros)}')


# -----------------------------------------------------------------
# Exercício 16 - vetor de 5 posições
# -----------------------------------------------------------------

numeros = []
for i in range(5):
    entrada = np.random.rand()
    numeros.append(float("{:.2f}".format(entrada)))
code_num = int(input("Digite uma das opções"
                     "\n0- para terminar; "
                     "\n1- para imprimir os números na ordem direta;"
                     "\n1- para imprimir os números na ordem indireta: "))
print(numeros)
if code_num == 0:
    print("programa terminado.")
elif code_num == 1:
    print(f"O vetor na ordem direta é {numeros}")
elif code_num == 2:
    print(f"O vetor na ordem inversa é {numeros[::-1]}")
else:
    print("Código inválido!")


# --------------------------------------------------------------------------------------
# Exercício 17 - lendo um vetor com 10 posições e atribuindo zero os elementos negativos
# ---------------------------------------------------------------------------------------

lista = []
nova_lista = []
for i in range(10):
    n = np.random.rand()
    if n > 0.5:
        lista.append(float("{:.2f}".format(n)))
    else:
        lista.append(-float("{:.2f}".format(n)))

for ele in lista:
    if ele < 0:
        ele = 0.00
        nova_lista.append(ele)
    else:
        nova_lista.append(ele)

print(lista)
print(nova_lista)


# --------------------------------------------------------------------------------------
# Exercício 18 - encontrando multiplos de um número em uma lista 
# ---------------------------------------------------------------------------------------

numeros = []

x = float(input('Digite um número: '))

for i in range(10):
    n = np.random.randint(1, 100)
    numeros.append(float("{:.2f}".format(n)))
print(numeros)

for ele in numeros:
    if float(ele) % x == 0:
        print(f'O {ele} é um multiplo de {x}.')



# -------------------------------------------------------------------------
# Exercício 19 - vetor com 50 posições cujos valores são (i+5*i) % (i+1)
# -------------------------------------------------------------------------

V = []

for i in range(5):
    V.append((i+5*i) % (i+1))
print(V)




# -------------------------------------------------------------------------
# Exercício 20 - Lendo numeros inteiros num intervalo de [0,50] e
# armazenando num vetor com 10 posições, e separando os valores que
# são ímpares e guardando-os em um outro vetor
# A saída imprime os elementos de cada vetor dois por linha
# ****************************** Melhorar as saída!!!
# -------------------------------------------------------------------------

numeros = []
impares = []

for i in range(10):
    n = np.random.randint(0, 51)
    numeros.append(n)
    if n % 2 != 0.0:
        impares.append(n)

print(numeros)
for i in range(1):
    print(f'numeros[0]= {numeros[i+0]}, numeros[1]={numeros[i+1]}')
    print(f'numeros[2]= {numeros[i+2]}, numeros[3]={numeros[i+3]}')
    print(f'numeros[4]= {numeros[i+4]}, numeros[5]={numeros[i+5]}')
    print(f'numeros[6]= {numeros[i+6]}, numeros[7]={numeros[i+7]}')
    print(f'numeros[8]= {numeros[i+8]}, numeros[9]={numeros[i+9]}')

# -------------------------------------------------------------------------
# Exercício 21 - subtração de vetores
# -------------------------------------------------------------------------
A = []
B = []
C = []
for i in range(10):
    A.append(np.random.randint(0, 100))
print(A)
for i in range(10):
    B.append(np.random.randint(0, 100))
print(B)
for i in range(len(A)):
    C.append(A[i] - B[i])
print(C)
# ----------------- Outra maneira com o list comprehension
# A = [np.random.randint(0, 100) for i in range(10)]
# print(A)
# B = [np.random.randint(0, 100) for i in range(10)]
# print(B)
# for i in range(len(A)):
#     C.append(A[i] - B[i])
# print(C)


# -------------------------------------------------------------------------
# Exercício 22 - compondo uma lista com elementos de outras duas listas
# -------------------------------------------------------------------------
A = []
B = []
C = []

for i in range(10):
    A.append(np.random.randint(0, 10))
print(A)
for i in range(10):
    B.append(np.random.randint(0, 10))
print(B)
for i in range(10):
    if i % 2 == 0:
        C.append(A[i])
    else:
        C.append(B[i])
print(C)
"""


# ---------------------------------------------------------
# Exercício 23 - produto escalar de dois conjuntos
# ---------------------------------------------------------

V1 = []
V2 = []
V1_dot_V2 = []
for i in range(5):
    n = np.random.randint(1, 100)
    V1.append(float("{:.2f}".format(n)))

for i in range(5):
    n = np.random.randint(1, 100)
    V2.append(float("{:.2f}".format(n)))

for i in range(5):
    V1_dot_V2.append(V1[i]*V2[i])

print(V1)
print(V2)
print(V1_dot_V2)


# ---------------------------------------------------------
# Exercício 24 - produto escalar de dois conjuntos
# ---------------------------------------------------------