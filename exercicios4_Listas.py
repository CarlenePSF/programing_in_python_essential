"""
Exercicios de listas
"""
#from random import randint

#import numpy as np


"""
#---------------------------------
# Exercicio 1 - 
# Fazer um programa que construa um vetor denominado A que armazena 6 numeros inteiros
# O programa deve executar os seguintes passo:
#(a) Atribua os valores 1, 0, 5, -2, -5, 7
#(b) Armazena em uma variável inteira a soma entre os valores das posições
#    A[0], A[1], A[5] do vetor e imprima na tela essa soma
#(c) Modifique o vetor na posição v[4] atribuindo a esta posição o valor 100
#(d) Mostre na tela cada valor do vetor A, um em cada linha
#---------------------------------

A = [1, 0, 5, -2, -5, 7]
print(A)
soma = A[0]+A[1]+A[5]
print(f'A soma dos elemento {A[0]}+{A[1]}+{A[5]} é {soma}')

A[4] = 100
for i in range(0, 6):
    print(f'{A[i]}')

#--------------------------------------------
# Exercicio 2 - lendo e imprimindo 6 valores inteiros
#-------------------------------------------

V = []
for i in range(0, 6):
    n = float(input(f'Entre com o elemento V[{i}]: '))
    V.append(n)
print(V)

#----------------------------------
# Exercicio 3 - Ler um conjunto de 10 numeros reais e armazene-os em um vetor.
# Calcule o quadrado das componentes desse vetor e armazene num novo vetor
# por fim imprima cada um dos vetores
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
# Programa para ler um vetor com 8 posições e, em seguida, ler dois valores
# x e y quaisquer que corresponda a duas posições no vetor. Imprima na tela a soma dos
# valores encontrado nas posições x,y fornecidas.
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
# Exercicio 5 - Contando elementos pare de um vetor
#--------------------------------------------------
v = []
soma = 0
for i in range(0, 10):
    a = randint(0, 10)
    v.append(a)
    if v[i] % 2 == 0:
        soma = soma+1

print(f'O vetor {v} tem {soma} elementos pares!.')

#-------------------------------------------------------------------
# Exercicio 6 - maior e menor elemento de um vetor com 10 posições
#-------------------------------------------------------------------

v = []
for i in range(0, 10):
    a = randint(0, 10)
    v.append(a)
ordenado = sorted(v)
print(f'O menor elemento de do vetor {v} e {ordenado[0]}')
print(f'O maior elemento do vetor {v} e {ordenado[9]}')
#print(f'O vetor {v} tem {soma} elementos pares!.')


#---------------------------------------------------------------------------
# Exercicio 7 - Imprimindo a posicao e o valor armazenado nessa posição que 
 corresponde ao maior elemento de um vetor
#---------------------------------------------------------------------------

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
# Exercicio 8 - Imprimindo vetor  com 6 posições em ordem inversa
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
# Exercicio 9 - Imprimindo os valores pares de um vetor com 6 posições
# em ordem inversa
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


#-----------------------------------------------------------------
# Exercicio 11 - 
# Imprimindo a quantidade de numeros negativos de um vetor com 10 posições
# Somando os elementos positivos desse vetor e retornando o resultado dessa soma
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


#-----------------------------------------------------------------
# Exercicio 12-13
# Fazer um programa que preencha um vetor com 5 valores e
# execute as seguintes tarefas
#1 - mostrar os valores lidos juntamente com o maior, o menor e a média dos valores
#2 - mostrar a posição onde se encontra o menor e o maior valor
#-----------------------------------------------------------------

v = []
soma = 0
for i in range(5):
    a = randint(0, 100)
    soma = soma + a
    v.append(a)
media = soma/len(v)
ordenado = sorted(v)


print(f'O vetor v gerado: {v}')
print(f'O maior elemento do vetor v: {ordenado[4]}')
print(f'O menor elemento do vetor v: {ordenado[0]}')
print(f'A média dos valores é {media}')

for i in range(5):
    if v[i] == ordenado[4]:
        print(f'A posicao do maior elemento {ordenado[4]}: v[{i}].')
    elif v[i] == ordenado[0]:
        print(f'A posição do menor elemento {ordenado[0]}: v[{i}].')
        

#-----------------------------------------------------------------
# Exercicio 14
# Verificando se existem elementos iguais numa lista com 10 posições
# e retornando quantas vezes esse valor é repetido
#-----------------------------------------------------------------

v = [2, 75, 2, 3, 57, 73, 63, 57, 15, 23]

'''
for i in range(10):
    a = randint(0, 100)
    v.append(a)
#testando com elementos repetidos
v[0] = 2
v[2] = 2
print(v)
'''
for i in v:
    if v.count(i) >= 2:
        print(f'O elemento {i} aparece {v.count(i)} na lista.')
    else:
        continue
"""


#------------------------------------------------------------------------------------
# Exercicio 15
# lendo uma lista com 20 posições, imprimindo a lista excluindo elementos repetidos
#------------------------------------------------------------------------------------

lista = [2, 75, 2, 3, 57, 73, 63, 57, 15, 23]

for i in lista:
    if lista.count(i) >= 2:
        conjunto = set(lista)

print(conjunto)
