"""
Lista de exercícios : trabalhando com loop
-> Uso de for, while, ranges, e break

Exercicios para revisar 30  , 33

"""

#from math import factorial
#from random import seed
#from random import randint



"""
#------------------------------------------------------
# Exercício 1 - multiplos de 3
#------------------------------------------------------
print(f'Os 5 primeiros multiplos de 3 sao:')
for n in range(1, 6):
    multiplo = 3*n
    print(multiplo)
 
#------------------------------------------------------
# Exercício 2 - 3 formas de executar loops
# imprimindo numeros de 1 a 100, de 1 em 1
#------------------------------------------------------
# 1- usando o for
for num in range(1, 101, 1):
    print(num)

#usando o while
n = 1
while n <= 100:
    print(n)
    n = n+1
#usando uma especie de do-while
i = 1
while True:
    print(i)
    i = i + 1
    if i > 100:
        break

#------------------------------------------------------
# Exercício 3 - contagem regressiva de 10 ate 0
# #----------------------------------------------------
num = 10
while num >= 0:
    print(num)
    num = num - 1
print('FIM!')


#------------------------------------------------------------------------
# Exercício 4 - imprimindo numeros de 1000 em 1000 menores do que 100000
# #----------------------------------------------------------------------

n = 0

while n < 100000:
    n = n + 1000
    print(n)


#---------------------------------------------------------------------
# Exercicio 5 - somando 10 numeros inseridos pelo usuario
#---------------------------------------------------------------------
v = []
soma = 0

for i in range(1, 11):
    n = int(input('Entre com um numero: '))
    v.append(n)
    soma = soma + n

print(v)
print(soma)


#---------------------------------------------------------------------
# Exercicio 6 - media de 10 numeros inteiros inseridos pelo usuario
#---------------------------------------------------------------------
v = []
media = 0
soma = 0

for i in range(1, 11):
    n = int(input('Entre com um numero: '))
    v.append(n)
    soma = soma + n
    media = soma/10

print(v)
print(soma)
print(media)


#---------------------------------------------------------------------------
# Exercicio 7 - media de 10 numeros inteiros positivos inseridos pelo usuario
# obs: Colocando uma condicao dentro do loop
#---------------------------------------------------------------------------

v = []
media = 0
soma = 0

for i in range(1, 11):
    n = int(input('Entre com um numero: '))
    if n > 0:
        v.append(n)
        soma = soma + n
        media = soma/10
    else:
        print('numero nao positivo inserido')
print(f'Os numero inseridos  foram {v}')
print(f'A media dos numeros positivos e {media}')


#-------------------------------------------------------------------------------
# Exercicio 8 - inserindo 10 numeros e retornando o menor e maior valor inseridos
# obs: Colocando uma condicao dentro do loop
#-------------------------------------------------------------------------------

v = []
for i in range(1, 11):
    n = int(input('Entre com um numero: '))
    v.append(n)
v.sort()
print(f'O menor valor digitado foi {v[0]}')
print(f'O maior valor digitado foi {v[9]}')

#-------------------------------------------------------------------------------
# Exercicio 9 - Imprimindo os N primeiro numeros naturais impares
#-------------------------------------------------------------------------------

N = int(input('Entre com um numero inteiro:'))
lista = []
i = 0
while i < N:
    i = i + 1
    if i % 2 != 0:
        lista.append(i)

print(lista)


#-------------------------------------------------------------------------------
# Exercicio 10 - Calculando a soma dos 50 primeiros numeros naturais
#-------------------------------------------------------------------------------
v = []
soma = 0
n = 0

while n < 50:
    n = n + 1
    if n % 2 == 0:
        v.append(n)
        soma = soma + n
print(v)
print(soma)


#---------------------------------------------------------------------------------
# Exercicio 11 - imprimindo os N primeiros numeros naturais em ordem crescente
#----------------------------------------------------------------------------------

N = int(input('Entre com um numero inteiro:'))
i = 0
for i in range(0, N+1, 1):
    print(i)


#-------------------------------------------------------------------------------
# Exercicio 12 - imprimindo os N primeiros numeros naturais em ordem decrescente
#-------------------------------------------------------------------------------

N = int(input('Entre com um numero inteiro:'))
i = 0
for i in range(N, -1, -1):
    print(i)



#-----------------------------------------------------------------------------------
# Exercicio 13 - imprimindo os N primeiros numeros naturais pares em ordem crescente
#-----------------------------------------------------------------------------------

N = int(input('Entre com um numero inteiro positivo par: '))
i = 0
for i in range(0, N+1, 1):
    if i % 2 == 0:
        print(i)

#-----------------------------------------------------------------------------------
# Exercicio 14 - imprimindo os N primeiros numeros naturais pares em ordem decrescente
#-----------------------------------------------------------------------------------

N = int(input('Entre com um numero inteiro positivo par: '))
i = 0
for i in range(N, -2, -1):
    if i % 2 == 0:
        print(i)

#----------------------------------------------------------------------------
# Exercício 15 - Imprimindo os N primeiros números ímpares ordem crescente
#----------------------------------------------------------------------------
N = int(input('Entre com um numero inteiro positivo: '))
i = 0
v = []
for i in range(1, N+1, 1):
    if i % 2 != 0:
        v.append(i)
print(f'Os primeiros números ímpares ate {N} são {v}')
#----------------------------------------------------------------------------
# Exercício 16 - Imprimindo os N primeiros números ímpares ordem decrescente
#----------------------------------------------------------------------------
N = int(input('Entre com um numero inteiro positivo: '))
i = 0
v = []
for i in range(N, 1, -1):
    if i % 2 != 0:
        v.append(i)
print(f'Os primeiros números ímpares ate {N} são {v}')

#----------------------------------------------------------------------------
# Exercício 17 - Imprimindo os N primeiros números ímpares ordem decrescente
#----------------------------------------------------------------------------

n = int(input('Entre com um numero inteiro positivo: '))
soma = 0
for i in range(1, n+1, 1):
    soma = soma+i
print(f'A soma dos {n} primeiros números naturais é {soma} ')


#----------------------------------------------------------------------------
# Exercício 18- Inserindo números e imprimindo o maior valor entre eles
#----------------------------------------------------------------------------

n = int(input('Digite a quantidade de números de entrada: '))
v = []
i = 1
while i < n+1:
    N = int(input('Digite um numero: '))
    v.append(N)
    i = i+1
v = sorted(v)
print(f'O maior valor digitado foi {v[n-1]} ')
print(f'O maior valor aparece {v.count(v[n-1])} vezes')

#--------------------------------------------------------------------------------
# Exercicio 19 - Imprimindo algarismos de um numero inteiro
#-------------------------------------------------------------------------------
num = input("Introduza um numero inteiro entre 100 e 999: ")

for i in range(0, 3):
    print(num[i])

#--------------------------------------------------------------------------------
# Exercicio 20 - Imprimindo algarismos de um numero inteiro
#-------------------------------------------------------------------------------

i = 0
cont = 0
total = 0
while i <= 100:
    i = i + 1
    num = int(input("entre com um numero: "))
    total = total + 1
    if num % 2 == 0:
        print(f"O numero digitado e par!")
        cont = cont+1
    elif num % 2 != 0:
        print("Numero impar")
    if num == 1000:
        break
print(f"A quantidade de numeros  digitados foi {total}")
print(f"A quantidade de numeros pares digitados foi {cont}")

#--------------------------------------------------------------------------------
# Exercicio 21 - Imprimindo algarismos de um numero inteiro
#-------------------------------------------------------------------------------

a = int(input("Entre com um valor inicial para o intervalo: "))
b = int(input("Entre com um valor final para o intervalo: "))
v = list(range(a, b+1, 1))
soma = 0
multi = 1
print(v)

for num in v:
    if num % 2 == 0:
        soma = soma + num
    elif num % 2 != 0:
        multi = multi*num
print(f"A soma dos numeros pares contidos no intervalo e {soma}")
print(f"O produto dos numero impares contidos no intervalo e {multi}")

#--------------------------------------------------------------------------------
# Exercicio 22 - calculando medias
#-------------------------------------------------------------------------------

media = 0.0
soma = 0.0
v = []
i = 0

while i < 5:
    nota = float(input("Entre com uma nota: "))
    if 10.0 <= nota <= 20.0:
        v.append(nota)
        soma = soma + nota
    else:
        print("Nota invalida!")
        break
    i = i+1
media = soma / i

print(v)
print(soma)
print(media)

#-------------------------------------------------------------------------------------------------------
# Exercicio 23 - calculando os divisores de um numero
# Se o numero for somente divisivel por 1 e por ele mesmo, com resto da divisao zero, e ele dito primo!
#-------------------------------------------------------------------------------------------------------
n = int(input("Entre com um numero positivo: "))
d = []

for i in range(1, n+1, 1):
    if n % i == 0:
        d.append(i)
print(f"Os divisores de {n}, incluindo ele mesmo, sao {d}")


#-------------------------------------------------------------------------------------------------------
# Exercicio 24 - calculando a soma dos divisores de um numero
# Se o numero for somente divisivel por 1 e por ele mesmo, com resto da divisao zero, e ele dito primo!
#-------------------------------------------------------------------------------------------------------
n = int(input("Entre com um numero positivo: "))
d = []
soma = 0

for i in range(1, n, 1):
    if n % i == 0:
        d.append(i)
        soma = soma + i
print(f"Os divisores de {n}, excluindo ele mesmo, são {d}")
print(f"A soma de todos os divisores de {n} é {soma}")

#-------------------------------------------------------------------------------------------------------
# Exercicio 25 - calculando a soma dos divisores 3 e 5 menores que 100
# Se o numero for somente divisivel por 1 e por ele mesmo, com resto da divisao zero, e ele dito primo!
#-------------------------------------------------------------------------------------------------------

i = 0
soma = 0.0
v = []

while i < 100:
    if i % 3 == 0 or i % 5 == 0:
        soma = soma + 1
        v.append(i)
    i = i+1
print(f"Todos os numeros naturais abaixo de 1000 que sao multiplos de 3 ou 5 sao {v}")
print(f"A soma deles e igual a {soma}")

#-------------------------------------------------------------------------------------------------------
# Exercicio 26 - calculando a soma dos divisores 3 e 5 menores que 100
# Se o numero for somente divisivel por 1 e por ele mesmo, com resto da divisao zero, e ele dito primo!
#-------------------------------------------------------------------------------------------------------

num = int(input("Entre com um numero: "))
v = []
 
for i in range(1, num+1):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        v.append(i)
        break
print(f"O primeiro multiplo de 11, 13 ou 17 e {v}")

#-------------------------------------------------------------------------------------------------------
# Exercicio 27 -Soma de uma serie harmonica
#-------------------------------------------------------------------------------------------------------
n = int(input("Entre com um valor: "))
soma = 0
i: int
for i in range(1, n+1, 1):
    soma = soma + 1/i
print(f"A soma da série harmônica é {soma}")

#-------------------------------------------------------------------------------------------------------
# Exercicio 28 -Soma da serie 1/N!
#-------------------------------------------------------------------------------------------------------
n = int(input("Entre com um valor: "))
soma = 0
v = list(range(1, n+1, 1))
i: int
for i in range(1, n+1, 1):
    soma = soma + 1/factorial(i)
print(soma)


#-------------------------------------------------------------------------------------------------------
# Exercicio 29 -Soma da serie 1/N! com 5 termos
#-------------------------------------------------------------------------------------------------------
i = 0

soma = 0.0
while i < 5:
    soma = soma + i/factorial(2*i)
    i = i+1
print(soma)


#-------------------------------------------------------------------------------------------------------
# Exercicio 30 - Soma de sequencias
# obs: verificar a soma2
#-------------------------------------------------------------------------------------------------------

n = int(input("Entre com um numero: "))

i = 1
soma1 = 0.0
soma2 = 0.0
soma3 = 0.0

while i <= n:
    soma1 = soma1 + i
    print(soma1)
    i = i+1

for j in range(1, n+1, 1):   #corrigir essa soma
    
    print(j)
    soma2 = soma2 - (2*j-1)
print(soma2)

for k in range(1, n+1, 1):
    soma3 = soma3 + (2*k-1)
    print(k)
    print(2*k-1)
    print(soma3)

#-------------------------------------------------------------------------------------------------------
# Exercicio 31 - Soma de sequencias
#-------------------------------------------------------------------------------------------------------
i = 0
soma = 0
while i <= 49:
    soma = soma + (2*i+1)/(i+1)
    print(i)
    i = i+1
print(soma)

#-------------------------------------------------------------------------------------------------------
# Exercicio 32 - sequencias de lançamento de um dado
#-------------------------------------------------------------------------------------------------------
# seed random number generator
seed()
# generate random integer values
for i in range(0, 6):
    a = randint(1, 6)
    b = randint(1, 6)
    print(f'Os numero dos lançamento dos dados são a={a}, b={b}.')
    if a > b:
        print("a > b")
    elif b > a:
        print("b > a")
    elif b == a:
        print("a = b")

#-------------------------------------------------------------------------------------------------------
# Exercicio 33 - multiplos de um número natural qualquer
# obs: ver esse exercicio 33!!!!!!!!!!!!!!
#-------------------------------------------------------------------------------------------------------
n = int(input("Entre com um valor (número natural) para n: "))
i = int(input("Entre com um valor para i (numero natural): "))
j = int(input("Entre com um valor para j (número natural): "))

for k in range(0, n, 1):
    if k % i == 0 or k % j == 0:
        print(k)
    elif k % i == 0 and k % j == 0:
        print(k)
"""
'''
#-------------------------------------------------------------------------------------------------------
# Exercicio 34 - 
#-------------------------------------------------------------------------------------------------------
p = 1

for q in range(1, 10):
    if p % q == 0:
        print(q)
    else:
        continue
'''
#---------------------------------------------------------------
# Exercicio 35 -
#---------------------------------------------------------------
'''
a = int(input("Inicio do intervalo: "))
b = int(input("Final do intervalo: "))

soma = 0
if a > b:
    print("Intervalo de valores invalido")
elif a < b:
    for i in range(a, b):
        if i % 2 != 0:
            soma = soma + i

if soma != 0:
    print(f'A soma dos numeros impares no intervalo de [{a},{b}] e {soma}')

#---------------------------------------------------------------
# Exercicio 36 - 
#---------------------------------------------------------------

n = 10
soma1 = 0
soma2 = 0
for i in range(1, n+1):
    soma1 = soma1 + i**2
    soma2 = soma2 + i
print(f'A soma do quadrado dos {n} primeiros numeros naturais e {soma1}')
print(f'O quadrado da soma dos {n} primeiros numeros naturais e {soma2**2}')
print(f'A diferenca entre esses valores e {soma2**2 - soma1}')
'''

#---------------------------------------------------------------
# Exercicio 37 - propriedade interessante de numeros com 4 algarismos
#---------------------------------------------------------------

'''
for i in range(1000, 10000):
    j = str(i)
    n = int(j[0:2])
    m = int(j[2:4])
    soma = n + m
    #print(n, m)
    #print(soma)
    if soma**2 == int(j):
        print(f'{soma**2} = {int(j)}')


#---------------------------------------------------------------
# Exercicio 38 -
#---------------------------------------------------------------
import matplotlib.pyplot as plt
soma = 0
x = []
y = []
c = []
for i in range(1, 500):
    for j in range(1, 500):
        for k in range(1, 500):
            if k**2 == i**2 + j**2 and k**2 < 250000:
                soma = (soma+1)
                x.append(i)
                y.append(j)
                c.append(k)

print(f'Foram encontrados {int(soma)} termos pitagoricos')
# Plot the data
plt.plot(x, y, '.', color='green')
# Add a legend
plt.legend()
# Show the plot
plt.show()
'''