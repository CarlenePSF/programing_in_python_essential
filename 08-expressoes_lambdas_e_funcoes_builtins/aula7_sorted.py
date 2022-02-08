"""
Sorted
OBS: Apesar do nome, não confunda com a função .sort() que já foi estudada com listas.sort()
     O método .sort() só funciona com listas!!!

Podemos utilizar o sorted com qualquer iterável.
Como o próprio nome diz o sorted() seve para ordenar elementos
     
# Relembrando o .sort()
lista = [1, 5, 4, 7, 2, 6, 9, 3, 8, 0]
print(lista)
lista.sort()
print(lista)

# usando o sorted() com lista
print(lista)
print(sorted(lista))

OBS: o sorted() SEMPRE RETORNA UMA LISTA com os elementos do iterável ordenados

# sorted() com tuplas
tupla = (1, 5, 4, 7, 2, 6, 9, 3, 8, 0)
print(tupla, type(tupla))
print(sorted(tupla), type(sorted(tupla)))

# sorted() com conjuntos
conjunto = {1, 5, 4, 7, 2, 6, 9, 3, 8, 0}
print(conjunto, type(conjunto))
print(sorted(conjunto), type(sorted(conjunto)))

# Adicionando parâmetros com o sorted()
numeros = [2, 7, 5, 6, 4, 1, 3]
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))  # ordena do maior para o menor


# ----------- Adicionando parâmetros com o sorted() --------------
numeros = [2, 7, 5, 6, 4, 1, 3]
print(numeros)

# Casting para tupla ou conjunto
print(tuple(sorted(numeros)))
print(set(sorted(numeros)))

# usando o reverse
print(sorted(numeros, reverse=True))  # ordena do maior para o menor


# ------------ Usando o sorted para tarefas mais complexas --------
# Ordenar pelo tamanho do dicionário
users = [
    {'username': "Sara", 'tweets': ["Python é legal!", "Mais mulheres no tech"]},
    {'username': "Samantha", 'tweets': []},
    {'username': "Nick", 'tweets': [], 'musica': 'Axé'},
    {'username': "Samuel", 'tweets': ["Fui selecionado para o BBB22! :O", "#Vamosjuntos#BBB22!"]},
    {'username': "Luna", 'tweets': ["#ForaBolsonaro", "#ForaBolsonaro"]},
    {'username': "Luana", 'tweets': ["#Salescaiu!", "#ForaBolsonaro"]},
    {'username': "John", 'tweets': [], 'cor': 'Amarelo', 'musica': 'Rock'},
    ]
print(users)
# Não aceita o dicionário diretamente
# print(sorted(users))

# ordenando em ordem alfabética de nomes
print(sorted(users, key=lambda usuario: usuario['username']))

# ordenando pelo número de tweets
print(sorted(users, key=lambda usuario: len(usuario['tweets'])))
"""

# Ultimo exemplo - umas lista de músicas
musicas = [
    {'titulo': 'Tenho medo', 'tocou': 6},
    {'titulo': 'Eu tenho  a senha', 'tocou': 15},
    {'titulo': 'Se for amor', 'tocou': 22},
    {'titulo': 'meu pedaço de pecado', 'tocou': 50}
]

#ordenando da menor tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# ordenando da mais tocadas para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
