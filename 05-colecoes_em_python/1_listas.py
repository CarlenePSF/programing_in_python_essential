"""
****************  Listas (list) em Python *************************

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferenca de serem DINAMICAS e tambem podemos colocar QUALQUER tipo de dado.

OBS:

- Linguagem C/Java: array
  - possuem tamanho e tipo de dado fixo:
     Se um array do tipo int for criado com tamanho 5,exemplo  int v[5],
     esse array sera SEMPRE do tipo inteiro e podera ter SEMPRE no maximo 5 valores.


- Em python:
   - as listas sao Dinamicas:
      Nao possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
   - as listas suportam Qualquer tipo de dado:
      Nao possui tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado
   - As listas em python sao representadas por colchetes []
     Exemplo: [1, 2, 3, 4]

Tipos de operacoes com listas

list1 = [1, 67, 33, 24, 56, 23]
list2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
list3 = []
list4 = list(range(1, 15, 1))
list5 = list('Geek University')
# Note que a list6 tem varios tipos de dados
list6 = ['programacao', 'em', 'python', 'essencial', 1, 2, 3, True, 'a', 'e', [2, 3, 4]]
cores = ['azul', 'verde', 'vermelho', 'branco', 'amarelo']

Podemos checar facilmente checar se determinado valor esta contido na lista

print(list1)
print(list2)
print(list3)
print(list5)

if 58 in list4:
    print('Encontrei o numero 8')
else:
    print('Nao encontrei o 8')



- podemos facilmente ordenar uma lista com a opcao .sort()
 como demonstrado abaixo:
list1.sort()
list2.sort()
print(list3)



- Podemos tambem contar o numero de ocorrencias de um valor em uma lista

print(list1.count(1))
print(list2.count('e'))



#- Para adicionar elementos em uma lista utilizamos a funcao append
#    No exemplo abaixo adicionamos o numero 33 a lista 1
#    Importante: com o append so podemos adicionar um elemento por vez!
#    Solucao:
#      - usar um loop
#      - colocar um outro objeto do tipo lista  sub-lista: lista.append(['a', 'b', 'c'])
#      - coloca cada elemento da lista como valor adicional: lista.extended([ 123, 23, 123])
      
print(list1)
list1.append(['a', 'b', 'c'])
print(list1)
for num in range(3):
    list1.append(num)
print(list1)


if 1 and 23 and 24 in list1:
    print('encontrei a lista')
else:
    print('nao encontrei a lista')

# - Adicionando elementos a uma lista

list1.extend([123, 234, 123])
list1.extend('Geek')
print(list1)    




#- Podemos tambem inserir um novo elemento na lista informado a posicao do indice.
#  Essa operacao nao substitui o valor inicial que se encontra na posicao,
#  ele e deslocado para a posicao seguinte

print(list1)
list1.insert(2, 'novo valor')
print(list1)


# - Podemos facilmente juntar duas listas
#   A soma de listas faz a mesma coisa que o extend()

list7 = list1 + list2
print(list7)

list1.extend(list2)
print(list1)



# Podemos inverter facilmente uma lista usando o reverse
print(list1)
print(list2)

list1.reverse()
list2.reverse()
print(list1)
print(list2)

# Essa forma abaixo segue o slice visto na aula de strings

print(list2[::-1])

# Copiando uma lista
list7 = list1.copy()
print(list1)
print(list7)


# tamanho de uma lista lista.len()
print(list1)
print(len(list1))



#Removendo o ultimo elemento de uma lista
# - o lista.pop() nao somente remove o ultimo elemento mas tambem o retorna
# - tambem podemos remover um elemento pelo indice basta especificar dentro do parentese qual posicao sera removida
# - Se nao existir elemento no indice informado, o programa da erro IndexError: pop index out of range
 
print(list2)
list2.pop()
print(list2)

list2.pop(2)
print(list2)

# A linha abaixo produz o erro IndexError
list2.pop(14)

# Limpando uma lista uma

print(list5)
list5.clear()
print(list5)

# Repetindo elementos de uma lista
nova = list1*2
print(nova)


# Convertendo uma string para uma lista
# obs: por padrao o split separa os elementos da lista pelo espaco entre as palavras
#---------------------------
# Exemplo 1
#---------------------------
curso = "Programacao em python essencial"
print(curso)
curso = curso.split()
print(curso)

#---------------------------
# Exemplo 2
#---------------------------

curso = "Programacao,em,python,essencial"
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista para uma string
# usando '(separador)'.join() transformamos a lista numa string com um separador especificado
#---------------------------
# Exemplo 1
#---------------------------

print(list6)
# Abaixo estamos ordenando que  toma a list6 e insira um espaco
# entre cada elemento depois transforme numa string
curso = ' '.join(list6)
print(curso)

# Abaixo estamos ordenando que  toma a list6 e insira um $
# entre cada elemento depois transforme numa string
curso = '$'.join(list6)
print(curso)


# -  Iterando sobre listas
#---------------------------------
# Exemplo 1 - usando o for
#---------------------------------
soma = 0
for item in list1:
    print(item)
    soma = soma + item
print(soma)

#---------------------------------
# Exemplo 1 - usando o while
#---------------------------------

carro = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carro.append(produto)

for produto in carro:
    print(produto)

#--------------------------------
# Utilizando variaveis em listas
#-------------------------------
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#-----------------------------------------------
# Fazendo acesso ao elementos a partir do indice
#           0        1        2
#cores = ['azul', 'verde', 'vermelho']
#-----------------------------------------------
cores = ['azul', 'verde', 'vermelho']
print(cores[0])
print(cores[1])

#--------------------------------------
#  Fazendo referencia de forma inversa
#           -3      -2          -1
# cores = ['azul', 'verde', 'vermelho']
# -------------------------------------
print(cores[-3])
print(cores[-2])


#-------------------
# loop em listas
#-------------------

cores = ['azul', 'verde', 'vermelho','branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice+1

#criou tuplas
cores = list(enumerate(cores))

# gerando indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

lista = []
lista.append(12)
lista.append(33)
lista.append(23)
print(lista)

# Outros metodos nao tao importantes mas tambem uteis

# encontrar o indice de um elemento na lista
numeros = [4, 5, 6, 7, 8, 5, 9, 10]

#em qual indice esta o valor 6 e 8
#print(numeros.index(6))
#print(numeros.index(8))


# OBS: caso nao tenha o elemento na lista um ero sera apresentado,
# como na linha abaixo
#print(numeros.index(34))

# OBS: elementos repetidos retorna o indice do primeiro elemento encontrado
#print(numeros.index(5))

# busca dentro de uma range(), ou seja, por qual indice comecar a buscar
#           0  1  2  3  4  5  6  7
#numeros = [4, 5, 6, 7, 8, 5, 9, 10]
#print(numeros.index(5, 3))


# Podemos fazer busca dentro de um range() com inicio/fim
# syntax : .index(element, ini, stop)
print(numeros.index(5, 3, 7))

# Revisando slicing
# lista[init:stop:step]
# range[init:stop:step]

#Trabalhando com o slice de lista com o parametro init
#        0  1  2  3  4  5  6  7
lista = [4, 5, 6, 7, 8, 5, 9, 10]
#inicionado no indice 1
print(lista[1:])

# usando o 'stop' i-1
print(lista[:5])

#usando o parametro 'step'
print(lista[::3])

# usando os 3 parametros init/stop/step

print(lista[1:6:2])


# invertendo valores em uma lista
# OSB: Para executar essa mesma troca em C seria necessario o uso de ponteiros

nomes = ['Carlene', 'Paula']
print(nomes)

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
#usando a funcao da biblioteca python
nomes.reverse()
print(nomes)


# Soma*, Valor máximo*, valor minimo*, tamanho
# * Se os valores forem todos inteiros (int) ou reais (float)

lista = [4, 5, 6, 7, 8, 5, 9, 10]
#soma
print(sum(lista))
#valor maximo
print(max(lista))
#valor minimo
print(min(lista))
#tamanho da lista
print(len(lista))

# Transformando um alista em tupla (a ,b)

lista = [4, 5, 6, 7, 8, 5, 9, 10]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#Desempacotando listas : util para ler arquivos
# OBS: se houver mais elementos do que variaveis para receber os valores,
# receberemos uma mensagem de erro
lista = [4, 5, 6]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)


# Copia de uma lista para outra (shallow copy and deep copy)

# Forma 1 -Deep copy

lista = [4, 5, 6]
print(lista)

nova = lista.copy()
print(nova)

nova.append(7)
print(lista)
print(nova)

# Veja que ao utilizarmos .copy() copiamos os dados de uma lista
# já definida para uma nova lista, que é independente da lista primária
# Isso em python é chamado de deep copy (ou cópia profunda)
"""
# Forma 2 - Shallow copy

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# OBS: Veja que utilizamos copia via atribuição copiando dados da antiga lista para uma nova lista.
# A modificação em uma das listas também é passada para a outra da qual a lista modificada foi feita.
