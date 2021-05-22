"""
Modulo collections: ordered dict
# Em um dicionario a ordem de insercao dos elementos nao e garantida
dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

print(dicionario)

for chave, valor in dicionario.items():
    print(chave, valor)

OrderedDict e um dicionario que nos garante a ORDEM de insercao dos elementos

# Fazendo o import
from collections import OrderedDict

dicionario2 = OrderedDict({'a': 1,  'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario2.items():
    print(chave, valor)
"""

# Fazendo o import
from collections import OrderedDict

# Entendendo a diferenca entre dict e Orderedict

#Criando dicionarios comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# sera que os dicionarios acima sao os mesmos??
# Sim, pois para um dicionario comum a ordem nao importa!
print(dict1 == dict2)

# Criando dicionarios com o ordered dict

dict01 = OrderedDict({'a': 1, 'b': 2})
dict02 = OrderedDict({'b': 2, 'a': 1})
# Sera que os dicionarios acima sao os mesmos??
# Nao eles nao sao, pois nesse caso a ordem importa!
print(dict01 == dict02)
