"""
Conjuntos

- Conjuntos em qualquer linguagem de programação é relacionado
  a teoria dos conjuntos na matemática.
- Em python, os conjuntos são chamados de sets. Ou seja, da mesma forma que na
matemática, os conjuntos em python terão as seguintes propriedades

 1 - Sets (conjuntos) não possuem valores duplicados
 2 - Sets não possuem valores ordenados
 3 - Elementos não são acessados via índice, ou seja, não podemos indexar
     conjuntos.


  - Conjuntos são bons para utilizar quando precisamos armazenar
    elementos, mas não nos importamos com a ordenação.
  - Quando não precisamos nos preocupar com chaves, valores e itens duplicados

Os conjuntos, ou sets, são referenciados em python com chaves {}

ATENÇÃO: Diferenca entre conjuntos (sets) e mapas (dicionários) em python:
     - Um dicionario tem chave/valor;
     - Um conjunto tem apenas valor;


# Definindo um conjunto

# Forma 1 - usando a funcao .set()

#note que o conjunto abaixo tem valores repetidos
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

#A linha abaixo mostra que quando imprimimos um conjunto,
# ele ignora, por definição, esses valores repetidos sem gerar erro
print(s)
print(type(s))

# Forma 2 - Forma literal

s2 = {1, 2, 3, 4, 5, 5, 6, 7, 2, 4}
print(s2)
print(type(s2))

#verificando se existe um elemento no conjunto
if 3 in s:
    print('tem o elemento 3')
else:
    print('Nao achei o elemento 3')

# Importante também lembrar que além de nao ter valores duplicados,
# também nao existe ordenamento num conjunto

# observe que lista e tuplas aceitam valores duplicados
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(lista)
print(type(lista), len(lista))

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(tupla)
print(type(tupla), len(tupla))


# Observe que dicionários e conjuntos nao aceitam chaves/elementos duplicados,
# respectivamente

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(dicionario)
print(type(dicionario), len(dicionario))


s = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(s)
print(type(s), len(s))

# Assim como qualquer conjunto, em python podemos colocar tipos de dados misturados em sets

s = {1, 2, 3, 'b', True, False, 'Geek'}
print(s)


# Iterando num set
for valor in s:
    print(valor)

# Uso interessante com conjuntos
# Suponha que realizemos o cadastro  de visitantes em uma feira ou museu
# e os visitantes informam manualmente a cidade de onde vieram.

# Podemos adicionar cada entrada da cidade em uma lista python,
# pois as listas aceitam elementos repetidos


cidades = ['Belo Horizonte', 'Sao Paulo', 'Bahia', 'Fortaleza', 'Fortaleza']
print(cidades)
print(len(cidades))

#Precisamos saber quantas cidades distintas temos
# podemos fazer um casting para transformar a lista em um set
cidades2 = set(cidades)

# Repare que o conjunto  nao mantem a ordenacao da sua criacao
print(cidades2)
print(len(cidades2))

### Adicionando elementos de um conjunto
# Notei que a ordem que ele imprime e aleatoria para cada chamada
conjunto = {'Belo Horizonte', 'Sao Paulo', 'Bahia', 'Fortaleza', 'Fortaleza'}
conjunto.add('Rio de Janeiro')
conjunto.add('Bahia')

print(conjunto)


### Removendo elementos de um conjunto
conjunto = {'Belo Horizonte', 'Sao Paulo', 'Bahia', 'Fortaleza', 'Fortaleza'}
print(conjunto)

# Forma 1 - usando .remove()
# Note que o argumento da .remove() nao e indice mas o valor!!
# pois conjuntos nao podem ser indexados

conjunto.remove('Fortaleza')
print(conjunto)
# OBS: Caso o valor nao seja encontrado sera gerado um erro Keyerror,
# como no exemplo abaixo
# conjunto.remove('Natal')

# Forma 2 - usando .discard()

conjunto.discard('Sao Paulo')
print(conjunto)

### Copiando um conjunto para outro...

conjunto = {'Belo Horizonte', 'Sao Paulo', 'Bahia', 'Fortaleza', 'Fortaleza'}
print(conjunto)

#Forma 1 - deepcopy
novo_conjunto = conjunto.copy()
novo_conjunto.add('Recife')
print(novo_conjunto)
print(conjunto)

# Forma 2 - Shallow copy

new_set = conjunto
new_set.add('Natal')

print(new_set)
print(conjunto)

#### Podemos remover todos os elementos de um conjunto

conjunto = {'Belo Horizonte', 'Sao Paulo', 'Bahia', 'Fortaleza', 'Fortaleza'}
print(conjunto)
conjunto.clear()
print(conjunto)

#### Metodos matematicos de conjuntos (operacao com conjuntos mesmas da matematica)

# Uniao de conjuntos
'''
Imagine que temos dois conjuntos: Um contem estudantes do curso de python,
outro contem estudantes do curso de java
Note que existe elementos iguais nos dois conjuntos
OBS: o set nao aceita soma de dois conjuntos como conjunto1 + conjunto2
'''

curso_python = {'Patricia', 'Marcelo', 'Henrique', 'Luiza', 'Carlene', 'Julia'}
print(curso_python)

curso_java = {'Marcelo', 'Luiza', 'Bruna', 'Carlos', 'Julia', 'Patricia'}
print(curso_java)

#Precisamos gerar um conjunto com os nomes dos estudantes unidos

'''
Forma 1 - Usando o union MAIS RECOMENDADO
'''
estudantes = curso_python.union(curso_java)
# note que nao geramos elementos repetidos, pois o conjunto ignora elementos repetidos
# O resultado {'Julia', 'Patricia', 'Luiza', 'Carlene', 'Carlos', 'Henrique', 'Bruna', 'Marcelo'}
# sera impresso abaixo
print(estudantes)

'''
Forma 2 - Utilizando o caractere pipe (|) - barra vertical
'''

estudantes2 = curso_python | curso_java
print(estudantes2)

# Intercessao entre conjuntos

'''
Forma 1 -
Precisamos gerar um conjunto com a intercessao entre os dois conjuntos
curso_python e curso_java. Para isso usamos a funcao .intersection()
'''

comum = curso_python.intersection(curso_java)
print(comum)

'''
Forma 2 -
 Usando o sinal de &
'''
comum2 = curso_python & curso_java
print(comum2)

# Gerando um conjunto com elementos que nao estao contidos no outro conjunto

'''
Forma 1 - usando . difference()
'''
so_python = curso_python.difference(curso_java)
print(so_python)

so_java = curso_java.difference(curso_python)
print(so_java)

'''** Note que a uniao do conjunto com os elementos em comum
e o conjunto dos elementos restantes que so estao em um conjunto especifico
produz o conjunto total
**'''
comum2 = curso_python & curso_java
print(comum2)

print(f'{curso_java == so_java.union(comum2)}')
print(f'{curso_python == so_python.union(comum2)}')

# Soma*, valor maximo*, valor minimo*, tamanho
# somente se os valores forem inteiros ou reais (float)
"""
conjunto = {1, 3, 5, 7, 9}

print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))
