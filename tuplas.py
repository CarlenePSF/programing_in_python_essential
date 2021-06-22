"""
Tuplas (tuple)

AS tuplas são bastante parecidas com as listas. Existem apenas duas diferenças básicas:
1 - As tuplas são representadas por parênteses
2 - As tuplas são imutáveis!!!  Ao se criar uma tupla ela não muda.
    Toda operação sobre uma tupla cria uma nova tupla.

# CUIDADO 1: As tuplas são representadas por parênteses (), mas veja:
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))


tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

#CUIDADO 2: Tuplas com 1 elemento

#Isso não é uma tupla, mesmo que esteja declarada entre parênteses
tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla3 = (4, )
print(tupla3)
print(type(tupla3))

#CONCLUSÃO: podemos concluir que tuplas são definidas pela vírgula, e não pelo parêntese
num = 1, 2
print(num)
print(type(num))

Resumindo:
(4) -> não é tupla
(4,)-> é tupla
4, -> é tupla


# Podemos gerar uma tupla dinamicamente com range(init, stop, step)
tupla = tuple(range(1, 6))
print(tupla)

# Desempacotamento de tupla
# OBS: Gera um value_error se colocarmos uma numero de elementos diferentes para desempacotar
tupla = ('Carlene', 'UFRN', 'física')
nome, escola, curso = tupla
print(nome)
print(escola)
print(curso)


#IMPORTANTE: Métodos para adição e remoção de elementos nas tuplas não existem, pois elas são imutáveis!!!

# Soma*, Valor máximo*, valor minimo*, tamanho
# * Se os valores forem todos inteiros (int) ou reais (float)
tupla = (1, 2, 3, 4, 5, 'string')
#soma
print(sum(tupla))
#valor maximo
print(max(tupla))
#valor minimo
print(min(tupla))
#tamanho da lista
print(len(tupla))


# Concatenando tuplas (juntar tuplas)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1)
print(tupla2)
#lembre-se tuplas são imutáveis
print(tupla1+tupla2)
print(tupla1)
print(tupla2)


#para modificar
tupla3 = tupla1+tupla2
print(tupla3)

# Mesmo, que as tuplas são imutáveis, mas podemos
# sobreescrever os seus valores, como demonstrado abaixo
tupla1 = tupla1+tupla2
print(tupla1)

# Verificando se um elemento esta contido na tupla

tupla = (1, 2, 3, 4, 5, 6)
#retornará um booleano true/false
print(3 in tupla)

#iterando sobre uma tupla


tupla = (1, 2, 3, 4, 5, 6)

for n in tupla:
    print(n)
for indice, valor in enumerate(tupla):
    print(indice, valor)

#contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'a', 'b')
print(tupla.count('c'))

nome = tuple('Carlene Paula')
print(nome)
print(nome.count('a'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisamos modificar os dados contidos numa coleção
# Exemplo 1

meses1 = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
          'novembro', 'dezembro')
i = 0
while i < len(meses1):
    print(meses1[i])
    i += 1

# checando indices
print(meses1.index('março'))
print(meses1.index('janeiro'))
# um item que não esta presente produz um erro
print(meses1.index('lua'))

# slicing
# sintaxe: tupla[init: stop: step]

meses1 = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
          'novembro', 'dezembro')

tupla2 = meses1[1: 12: 2]
print(tupla2)


#-------------------------------------
# Porque Utilizar tuplas, então?
#-------------------------------------

1 - Tuplas são mais rápidas do que listas
2- tuplas deixam o código mais seguro, pois trabalhar com elementos imutáveis traz mais segurança para o código!


# Copiando uma tupla para outra
tupla = (1, 2, 3, 4, 5)
#print(tupla)

nova = tupla
#print(nova)
#print(tupla)


# IMPORTANTE: Na tupla não tem problema de shallow copy
outra = nova
nova = nova + outra
print(nova)
"""

