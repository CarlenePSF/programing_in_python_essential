"""
Lista de exercícios : trabalhando com loop
-> Uso de for, while, ranges, e break

Exercicios para revisar 30  , 33

"""

# from math import factorial
# from random import seed
# from random import randint
# import matplotlib.pyplot as plt
# from random import randint, seed
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

#-------------------------------------------------------------------------------------------------------
# Exercicio 34 - 
#-------------------------------------------------------------------------------------------------------
p = 1

for q in range(1, 10):
    if p % q == 0:
        print(q)
    else:
        continue

#---------------------------------------------------------------
# Exercicio 35 -
#---------------------------------------------------------------

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

#---------------------------------------------------------------
# Exercicio 37 - propriedade interessante de numeros com 4 algarismos
#---------------------------------------------------------------


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

soma = 0
x = []
y = []
c = []
for i in range(1, 334):
    for j in range(1, 334):
        for k in range(1, 334):
            if k**2 == i**2 + j**2 and k**2 < 111556:
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


#---------------------------------------------------------------
# Exercicio 39 - Calcular a base de um triangulo
#---------------------------------------------------------------

base = float(input("Digite o valor para a base: "))
altura = float(input("Digite o valor para altura: "))


#---------------------------------------------------------------
# Exercicio 40 - lendo numeros inteiros
#---------------------------------------------------------------

n = 0
v = []
while n >= 0:
    n = int(input("Digite um numero: "))
    v.append(n)
lista = v.pop()
print((sorted(lista)))
print(f'O menor valor digitado foi {min(lista)}')
print(f'O maior valor digitado foi {max(lista)}')


#---------------------------------------------------------------
# Exercicio 41 - Associacao em paralelo de dois resistores
#---------------------------------------------------------------
R1 = 1
R2 = 1
while R1 != 0 and R2 != 0:
    R1 = int(input("Entre com a resistencia R1: "))
    R2 = int(input("Entre com a resistencia R2: "))
    if R1 != 0 and R2 != 0:
        R = (R1*R2)/(R1+R2)
        print(f'A resistencia total e {R}')
    else:
        break

#---------------------------------------------------------------
# Exercicio 42 - loop para calcular quadrado/cubo/raiz quadrada
#---------------------------------------------------------------
n = 1
while n > 0:
    n = int(input("entre com um valor: "))
    if n > 0:
        print(f'O quadrado de {n} e {n*n}')
        print(f'O cubo de {n} e {n*n*n}')
        print(f'A raiz quadrada de {n} e {n**(1/2)}')
    else:
        break
        

#---------------------------------------------------------------
# Exercicio 43 - media de idade de determinado grupo 
#---------------------------------------------------------------
idade = 1
soma = 0
n = 0
media = 0

while idade != 0:
    idade = int(input("Entre com a idade: "))
    if idade > 0:
        soma = soma+idade
        n = n+1
    elif idade <= 0:
        break
media = soma/n
print(f'A media de idade do grupo e {int(media)}')


#---------------------------------------------------------------
# Exercicio 44 - Sequencia Fibonacci de um numero
#---------------------------------------------------------------

n = int(input("Entre com um numero positivo: "))

# first two terms
n1, n2 = 0, 1

for i in range(2*n):
    print(f'{i}:{n1}')
    nth = n1 + n2
    if n1 > n:
        break
    else:
        n1 = n2
        n2 = nth

#---------------------------------------------------------------
# Exercicio 45 - conversor de velocidade
#---------------------------------------------------------------

converte = True

while converte:
    unidade = int(input("Digite 1: km/h -> m/s ou 2: m/s -> km/h: "))
    if unidade == 1:
        velocidade = float(input("Qual a velocidade? "))
        print(f'A velocidade em m/s é {velocidade/3.6}')
    elif unidade == 2:
        velocidade = float(input("Qual a velocidade? "))
        print(f'A velocidade em km/h é {velocidade*3.6}')
    converte = int(input("Digite 0 para sair ou 1 para continuar a converter:"))
    if converte == 1:
        continue
    elif converte == 0:
        break


#------------------------------------------------------------------
# Exercicio 46 - jogo da sorte com um pseudorandom number generator
#------------------------------------------------------------------

seed()

tentativa = 1
valor = 1
while True:
    num = int(input("Escolha um numero de 1 a 10: "))
    valor = randint(1, 10)
    print(valor)
    if num == valor:
        print(f' Parabéns, você ganhou! Sua escolha foi {num} e o sorteiro foi {valor}')
        print(f'Você acertou com {tentativa} tentativas')
        break
    elif num < valor:
        print(f' Desculpe! tente novamente, pois seu chute foi menor que o valor sorteado!')
    elif num > valor:
        print(f'Desculpe! tente novamente, pois seu chute foi maior que o valor sorteado!')
    tentativa = tentativa+1

# ---------------------------------------------------------------
# Exercicio 47 - calculadora
# ---------------------------------------------------------------

while True:
    num1 = float(input("Entre com um  numero: "))
    num2 = float(input("Entre com outro numero: "))
    print("escolha uma das operacoes abaixo. ")
    print("1 - adicao")
    print("2 - subtracao")
    print("3 - multiplicacao")
    print("4 - divisao")
    print("5 - sair")
    op = int(input("Digite sua escolha: "))

    if op == 1:
        print(f'A soma de {num1} e {num2} e {num1 + num2}')
    elif op == 2:
        if num1 > num2:
            print(f'A diferenca de {num1} e {num2} e {num1 - num2}')
        else:
            print(f'A diferenca de {num1} e {num2} e {num2 - num1}')
    elif op == 3:
        print(f'O produto de {num1} com {num2} e {num1 * num2}')
    elif op == 4:
        if num2 != 0:
            print(f'A divisao entre {num1} por {num2} e  {num1 / num2}')
        else:
            print("Denominador igual a zero. Divisao nao e definida")
    else:
        break


#----------------------------------------------------------------------------------
# Exercicio 48 - Somando os numeros pares da sequencia Fibonacci menores do que 4e^6
#---------------------------------------------------------------------------------


N = 35
# first two terms of the Fibonacci sequence
n1, n2 = 0, 1
soma = 0

v = []
fibonacci = []


for i in range(N):
    fibonacci.append(n1)
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    if n1 % 2 == 0:
        soma = soma + n1
        v.append(n1)

print(fibonacci)
print(f'Os elementos pares da sequencia sao {v}')
print(f'A soma dos numeros pares da sequencia e {soma}')


N = 35
# first two terms of the Fibonacci sequence
n1, n2 = 0, 1
fibonacci = []
for i in range(N):
    fibonacci.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth


print(fibonacci)
"""

#------------------------------------------------------------------------------------
# Exercicio 49 - Aplicacoes em caderneta de poupanca Pensarr
#------------------------------------------------------------------------------------

salario_carlos = float(input("Carlos, entre com o salario recebido do mes : "))
salario_joao = (1. / 3.) * salario_carlos
print(salario_joao)
mes = 1
rendimento_carlos = salario_carlos*0.02
rendimento_joao = salario_joao*0.05

retorno_joao = 0
retorno_carlos = 0

while rendimento_joao < rendimento_carlos:
    rendimento_joao = rendimento_joao + 0.05*rendimento_joao
    rendimento_carlos = rendimento_carlos + 0.02*rendimento_carlos
    mes = mes+1

    retorno_joao = rendimento_joao
    retorno_carlos = rendimento_carlos
    if retorno_joao >= retorno_carlos:
        break


print(f'Apos {mes} meses o rendimento de Joao ultrapassou o de Carlos')
print(f'João recebera ao total {retorno_joao}')
print(f'Carlos recebera ao total {retorno_carlos}')



#------------------------------------------------------------------------------------
# Exercicio 50 -
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
# Exercicio 51 -
# #------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
# Exercicio 52 - Somando os numeros pares da sequencia Fibonacci menores do que 4e^6
#-----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
# Exercicio 53 - Somando os numeros pares da sequencia Fibonacci menores do que 4e^6
#-----------------------------------------------------------------------------------
