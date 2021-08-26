"""
Exercícios de listas, tuplas, dicionário, sets
"""
from random import seed
# import random
import numpy as np
# from math import sqrt
# seed random number generator
np.random.seed(21)
seed(25)
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
# Exercício 24 - comparando alturas entre alunos
# ---------------------------------------------------------
i = 0
dados = []
# Gerando os IDs aleatoriamente
ID = random.sample(range(1, 100), 10)
print(ID)

# Gerando os dados da altura aleatoriamente
while i <= 9:
    alturas = 1.5+np.random.rand()
    entradas = [ID[i],  float("{:.2f}".format(alturas))]
    dados.append(entradas)
    i += 1
print(dados)

alturas = sorted([dados[i][1] for i in range(len(dados))])

for i in range(10):
    if alturas[0] == dados[i][1]:
        print(f'O aluno mais baixo mede {alturas[0]} e tem ID = {dados[i][0]}')
    elif alturas[9] == dados[i][1]:
        print(f'O aluno mais alto mede {alturas[9]} e tem ID = {dados[i][0]}')


# ---------------------------------------------------------
# Exercício 25 - os primeiros 100 números que não são multiplos de 7 e nem terminam em 7
# ---------------------------------------------------------
step = 12
not_seven_multiples = []
while len(not_seven_multiples) < 100:
    step = step+1
    string = str(step)
    if step % 7 != 0 and string[-1] != '7':
        not_seven_multiples.append(step)
print(not_seven_multiples)


# ---------------------------------------------------------
# Exercício 26 - desvio padrão
# ---------------------------------------------------------
numeros = random.sample(range(1, 50), 10)
media = sum(numeros)/len(numeros)
soma = 0
for element in numeros:
    soma += (element-media)**2
desvio_padrao = sqrt((1/(len(numeros)-1)) * soma)
print(f'O desvio padrão da amostra {numeros} é: ')
print(float("{:.2f}".format(desvio_padrao)))



# ---------------------------------------------------------
# Exercício 27 - imprimindo números primos --- revisar!!!!
# ---------------------------------------------------------

numeros_aleatorios = random.sample(range(1, 11), 10)
print(numeros_aleatorios)

primos = []

for indice, elemento in enumerate(numeros_aleatorios):
    if elemento > 1:
        for i in range(2, elemento):
            if elemento % i == 0:
                print(elemento, "is not a prime number because", i, "times", elemento // i, "is", elemento)
                break
            else:
                print(f'O número {elemento} é primo e está na posição {indice}')
                break


# ---------------------------------------------------------
# Exercício 28 -
# ---------------------------------------------------------

mais_numeros = random.sample(range(1, 11), 10)
print(mais_numeros)

pares = []
impares =[]

for elemento in mais_numeros:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)

print(f'Elementos pares de V são: {pares}')
print(f'Elementos impares de V são: {impares}')

# ---------------------------------------------------------
# Exercício 29 -
# ---------------------------------------------------------

inteiros = random.sample(range(1, 100), 6)
print(inteiros)
pares2 = []
impares2 = []

for elemento in inteiros:
    if elemento % 2 == 0:
        pares2.append(elemento)
    else:
        impares2.append(elemento)

print(f'Elementos pares  são: {pares2}. A soma deles é {sum(pares2)}')
print(f'Elementos impares são: {impares2}. A lista contém {len(impares2)} elementos.')

# ---------------------------------------------------------
# Exercício 30 -
# ---------------------------------------------------------
vetor1 = random.sample(range(1, 100), 10)
vetor2 = random.sample(range(1, 100), 10)
print(sorted(vetor1), sorted(vetor2))
intersection = []

for element1 in vetor1:
    if element1 in vetor2:
        intersection.append(element1)
print(intersection)


# ---------------------------------------------------------
# Exercício 31 -
# ---------------------------------------------------------
vetor1 = random.sample(range(1, 100), 10)
vetor2 = random.sample(range(1, 100), 10)
print(f'Os elementos do vetor 1 são {sorted(vetor1)}')
print(f'Os elementos do vetor 2 são {sorted(vetor2)}')
union = [i for i in vetor1]
for element in vetor2:
    union.append(element)

union = list(set(union))
print(f'A união dessas listas é {sorted(union)}')


# ---------------------------------------------------------
# Exercício 32 -
# ---------------------------------------------------------
x = random.sample(range(1, 15), 5)
y = random.sample(range(1, 15), 5)
print(x, y)
soma_vetorial = []
produto_escalar = []
complementar = []
intersecao = []
for i in range(5):
    soma = x[i]+y[i]
    prod = x[i]*y[i]
    soma_vetorial.append(soma)
    produto_escalar.append(prod)
    if x[i] not in y:
        complementar.append(x[i])
    elif x[i] in y:
        intersecao.append(x[i])
    elif y[i] in x:
        intersecao.append(y[i])


uniao = [i for i in x]
for element in y:
    uniao.append(element)
uniao = list(set(uniao))

print(f'A soma de x e y é {soma_vetorial}')
print(f'O produto escalar entre x e y é {produto_escalar}')
print(f'Os elementos que estão em x mas não estão em y são {complementar}')
print(f'A interseção entre x e y é {intersecao}')
print(f'A união dessas x e y é {sorted(uniao)}')


# ---------------------------------------------------------
# Exercício 33 -
# ---------------------------------------------------------
x = [random.randint(0, 10) for i in range(15)]
print(x)
for i, element in enumerate(x):
    if element == 0:
        x.pop(i)

print(x)



# ---------------------------------------------------------
# Exercício 34 -
# ---------------------------------------------------------
numeros = []
for i in range(10):
    entrada = float(input("digite um numero: "))
    if i == 0:
        numeros.append(entrada)
    elif entrada in numeros:
        entrada = float(input("Numero ja existe na lista! Por favor insira outro numero: "))
        numeros.append(entrada)
    else:
        numeros.append(entrada)
print(numeros)


# ---------------------------------------------------------
# Exercício 35 -
# ---------------------------------------------------------


# ---------------------------------------------------------
# Exercício 36 - 
# ---------------------------------------------------------

reais = []
for i in range(10):
    entrada = float(input("digite um numero: "))
    if i == 0:
        reais.append(entrada)
    elif entrada in reais:
        entrada = float(input("Numero ja existe na lista! Por favor insira outro numero: "))
        reais.append(entrada)
    else:
        reais.append(entrada)
print(reais)
reais.sort()
print(reais)


# ---------------------------------------------------------
# Exercício 37 - vetor com 11 elementos
#  ordenado tal que a1 < a2 < a3 ... < a6 > a7 > a8
# ---------------------------------------------------------

vetor = [45.0, 448.0, 256.0, 2.0, 5.0, 5.5, 75.0, 63.0, 15.0, 984.0, 487]
final = []
ordenado_crescente = sorted(vetor.copy())
ordenado_decrescente = sorted(vetor.copy(), reverse=True)

#print(ordenado_crescente, ordenado_decrescente)

for i in range(6):
    final.append(ordenado_crescente[i])
for i in range(5):
    final.append(ordenado_decrescente[i])

print(final)

# ---------------------------------------------------------
# Exercício 38 -
# ---------------------------------------------------------

reais = []
for i in range(10):
    entrada = float(input("digite um numero: "))
    reais.append(entrada)
    reais.sort()

print(reais)
"""
# ---------------------------------------------------------
# Exercício 39 - Triângulo de Pascal
# ---------------------------------------------------------


def calcula_posicao(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return int(calcula_posicao(n - 1, k - 1)) + int(calcula_posicao(n - 1, k))


print(int(calcula_posicao(6, 5)))


def pascalLine(linhas):
    linhas = linhas + 1
    triangulo = []

    for linha in range(linhas):
        valores_linha = []

        for coluna in range(linha + 1):
            valores_linha.append(calcula_posicao(linha, coluna))

        triangulo.append(valores_linha)

    return triangulo


imprime = pascalLine(5)
for i in range(len(imprime)):
    print(imprime[i])
