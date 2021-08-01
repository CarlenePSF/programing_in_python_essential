"""
Min e Max

*** max() - > retorna o maior valor em um iterável ou o maior valor de dois ou mais elementos

# Exemplo 1 - lista
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

# Exemplo 2 - tupla
tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

# Exemplo 3 - conjunto
conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

# Exemplo 4 - dicionário
dicionario = {'a': 1,
              'b': 8,
              'c': 4,
              'd': 99,
              'e': 34,
              'f': 129
              }
print(max(dicionario))  # retorna a chave
print(max(dicionario.values()))  # retorna o valor associado a chave


# Passando dois valores quaisquer
# print(max(3, 34))

# Faça um programa que receba dois valores do usurário e informe o maior dentre eles
val1 = int(input('Informe um valor: '))
val2 = int(input('Informe outro valor: '))
print(f'O maior dos valores informados é {max(val1, val2)}')


# podemos passar quantos valores quisermos e com diferentes tipos de dados
print(max(3, 56, 1))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'z'))
print(max(3.1415, 34.66))
print(max('Carlene'))

*** min() --> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos


# Exemplo 1 - lista
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

# Exemplo 2 - tupla
tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

# Exemplo 3 - conjunto
conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

# Exemplo 4 - dicionário
dicionario = {'a': 1,
              'b': 8,
              'c': 4,
              'd': 99,
              'e': 34,
              'f': 129
              }
print(min(dicionario))  # retorna a chave
print(min(dicionario.values()))  # retorna o valor associado a chave


# Passando dois valores quaisquer
# print(max(3, 34))

# Faça um programa que receba dois valores do usurário e informe o maior dentre eles
val1 = int(input('Informe um valor: '))
val2 = int(input('Informe outro valor: '))
print(f'O maior dos valores informados é {min(val1, val2)}')


# podemos passar quantos valores quisermos e com diferentes tipos de dados
print(min(3, 56, 1))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'z'))
print(min(3.1415, 34.66))
print(min('Carlene'))



# Exemplos mais complexos
nomes = ['Amanda', 'Bruna', 'Carlos', 'Raíssa', 'Daniel']
print(max(nomes))
print(min(nomes))

# Usando uma expressao lambda
# para cada nome da lista de nomes ordenamos pelo tamanho do nome
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""

# Exemplo de umas lista de músicas
musicas = [
    {'titulo': 'Tenho medo', 'tocou': 6},
    {'titulo': 'Eu tenho  a senha', 'tocou': 15},
    {'titulo': 'Se for amor', 'tocou': 22},
    {'titulo': 'Meu pedaço de pecado', 'tocou': 50}
]
# pegando a musica que mais tocou
print(max(musicas, key=lambda musica: musica['tocou']))
# pegando a musica que menos tocou
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio 1
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
# pegando a musica que menos tocou
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Desafio 2 - Como encontrar a musica mais tocada e a menos tocada sem usar max min e lambdas
maximo = 0
for musica in musicas:
    if musica['tocou'] > maximo:
        maximo = musica['tocou']
for musica in musicas:
    if musica['tocou'] == maximo:
        print(musica['titulo'])


minimo = 100
for musica in musicas:
    if musica['tocou'] < minimo:
        minimo = musica['tocou']
for musica in musicas:
    if musica['tocou'] == minimo:
        print(musica['titulo'])