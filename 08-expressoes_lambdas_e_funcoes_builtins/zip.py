"""
Zip

zip() --> Cria um iterável chamado zip object que recebe como entrada os elemento de cada um dos iteráveis, e retorna
         esses elementos em pares


# --------------------- Exemplos ----------------------------
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

zip_1 = zip(lista_1, lista_2, 'abc')
print(zip_1)
print(type(zip_1))

# A partir de um zip, podemos gerar dados tipo lista, tupla, conjunto ou dicionario
print(list(zip(lista_1, lista_2)))
print(tuple(zip(lista_1, lista_2)))
print(set(zip(lista_1, lista_2)))
print(dict(zip(lista_1, lista_2)))

OBS: Assim que o objeto for convertido em algum tipo de dado ele e excluido da memoria
     o mesmo ocorreu com o map, filter e o generator.

O zip utiliza como parâmetro o comprimento (len) do menor iterável. Se o iterável tiver tamanhos diferentes
a quantidade de pares formados sera correspondente ao numero de elementos do menos iterável. Veja o exemplo abaixo.

print(list(zip(lista_1, lista_2, 'abcde')))
print(tuple(zip(lista_1, lista_2, 'abcde')))
print(set(zip(lista_1, lista_2, 'abc')))
"""

# Podemos usar diferentes iteraveis com o zip
# 1 - Passando tuplas e listas
tupla1 = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionarios = {
    'a': 11,
    'b': 12,
    'c': 13,
    'd': 14,
    'e': 15
}

print(list(zip(tupla1, lista, dicionarios.values())))

# Passado uma lista de tuplas
dados = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(list(zip(*dados)))


# ----------- Exemplos mais complexos ---------
# O zip e util para juntar vários dados
prova1 = [80, 91, 78]
prova2 = [98, 99, 45]
alunos = ('Maria', 'Calos', 'Joanna')

# dict comprehension
notas = {dado[0]: (dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(notas)
print(final)

# ------ Outra maneira usando a funcao map() ---------
# primeiro fazemos o zip das prova1 e prova 2
# depois e executado o map do objeto zip() extraindo a nota maxima
# depois criamos outro objeto zip que mapeia os alunos para cada nota maxima

final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final2))
