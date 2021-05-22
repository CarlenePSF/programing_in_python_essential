"""
Modulo collection - Named Tuple

#recapitulando tupla
tupla = (1, 2, 3)
print(tupla[0])

Named tuple -> São tuplas diferenciadas das tuplas convencionais, onde especificamos um nome para a mesma
 como também parâmetros
"""

#Importando pacotes
from collections import namedtuple

#Definindo o nome e parametros

#Forma 1
#>>> cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2 -
#>>> cachorro = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3 - Mais clara colocando os parâmetros na lista
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# produto para uma loja
tenis = namedtuple('tenis', ['tamanho', 'marca', 'modelo'])


#Usando as variaveis definidas com parametros atribuidos por mim

sucata = cachorro(idade=2, raca='bigle', nome='sucata')
print(sucata)
print(f'Idade do cachorro: {sucata[0]}')
print(f'Raça do cachorro: {sucata[1]}')
print(f'Nome do cachorro: {sucata[2]}')
print('\n')

#produto de uma loja de tênis
rush_one = tenis(tamanho=36, marca='adidas', modelo='rush-one')
print(rush_one)

#Acessando os dados - forma 1
print(f'Tamanho do tênis: {rush_one[0]}')
print(f'Marca do tênis: {rush_one[1]}')
print(f'Modelo do tênis: {rush_one[2]}')

#Acessando os dados - Forma 2
print(sucata.idade)
print(sucata.raca)
print(sucata.nome)

#Acessando os dados - forma 3
#OBS: Todos os atributos de listas/tuplas /colecoes/ dicionarios podem ser usados aqui
print(sucata.index(2))
print(sucata.index('bigle'))
