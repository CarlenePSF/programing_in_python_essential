"""
Modulo collections - counter (contador)
As coleções builtin do python sao listas, tuplas, conjuntos, dicionários
Existe um modo especial no python conhecido como collections que fornece
uma alternativa para as coleções ja estudadas

Collection e conhecido  como high-performance container Datatype

counter - recebe um iterável como parâmetro e cria um objeto do tipo Collections counter
          que e parecido com um dicionario, contendo o elemento de lista passado como
          parâmetro e como valor e quantidade de ocorrências desse elemento

#****** podemos utilizar qualquer iterável!! No exemplo abaixo usamos uma lista ******
lista = [2, 4, 5, 1, 1, 1, 3, 3, 3, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9]
cores = ['azul', 'verde', 'azul', 'vermelho', 'Azul', 'verde', 'amarelo']

# Exemplo 1
res_lista = Counter(lista)
res_string = Counter(cores)

print(type(res_lista))
print(type(cores))

# Imprime a quantidade de ocorrências de cada elemento na lista
print(res_lista)
#>>> Counter({6: 4, 1: 3, 3: 3, 7: 3, 8: 3, 2: 1, 4: 1, 5: 1, 9: 1})


#Note que o python e case sensitive, distinguindo a string 'azul' de 'Azul'
print(res_string)
# >>> Counter({'azul': 2, 'verde': 2, 'vermelho': 1, 'Azul': 1, 'amarelo': 1})

#Exemplo 2 - passando uma string

print(Counter('Geek University'))
"""

# Importando a biblioteca

from collections import Counter

# Exemplo 3 -

texto = """ Python is an interpreted high-level general-purpose programming language. 
            Python's design philosophy emphasizes code readability with its notable 
            use of significant indentation. Its language constructs as well as its 
            object-oriented approach aim to help programmers write clear, 
            logical code for small and large-scale projects. Python is dynamically-typed 
            and garbage-collected. It supports multiple programming paradigms, 
            including structured (particularly, procedural), object-oriented 
            and functional programming. Python is often described as a "batteries included" 
            language due to its comprehensive standard library. Guido van Rossum 
            began working on Python in the late 1980s, as a successor to the ABC 
            programming language, and first released it in 1991 as Python 0.9.0.
            Python 2.0 was released in 2000 and introduced new features, such as 
            list comprehensions and a garbage collection system using reference counting. 
            Python 3.0 was released in 2008 and was a major revision of the language that 
            is not completely backward-compatible and much Python 2 code does not run 
            unmodified on Python 3. Python 2 was discontinued with version 2.7.18 in 2020.
            Python consistently ranks as one of the most popular programming languages """


texto2 = """Quantum spin liquids (QSLs) - a magnetic analog of the fractional quantum Hall 
           liquid - epitomize key notions of modern condensed matter physics. These include 
           fractionalization of elementary excitations, topological order, and emergent 
           gauge fields. From a magnetic phase viewpoint, QSLs are qualitatively different
           from conventional symmetry-broken states of matter as their ground state 
           wave-function is characterized by long-range quantum entanglement between 
           local degrees of freedom. The topological character of QSLs is manifested in 
           quasiparticle excitations carrying fractional quantum numbers and non-local 
           statistical interactions for a special class of QSLs. Such quasiparticles 
           cannot be created in a single isolated form but only in multiple pairs.
           
           Broadly speaking, QSLs emerge in spin systems where the corresponding classical
           model has a macroscopic ground state degeneracy. Strong thermal and quantum 
           fluctuations induced by the macroscopic degeneracy disrupt the development of 
           long-range magnetic order. This approach has been pursued for geometrically 
           frustrated magnets made of corner-sharing triangles or tetrahedral. The 
           canonical example in two dimensions is a nearest-neighbor (nn) Heisenberg model
           on the kagome lattice (=a lattice of corner-sharing triangles). In the kagome
           lattice, continuous rotations of spin clusters can be generated without 
           incurring an energy cost, thereby leading to a destabilization of classical 
           magnetic order. """

palavras_texto1 = texto.split()
print(palavras_texto1)

res_texto1 = Counter(palavras_texto1)
print(res_texto1)

# encontrando as palavras com mais de 5 ocorrências no texto 1
print(res_texto1.most_common(5))


palavras_texto2 = texto2.split()

res_texto2 = Counter(palavras_texto2)
print(res_texto2)

# encontrando as palavras com mais de 5 ocorrências no texto 2
print(res_texto2.most_common(5))
