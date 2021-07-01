"""
Modulo collections: ordered dict
# Em um dicionario a ordem de inserção dos elementos nao e garantida
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

OrderedDict e um dicionario que nos garante a ORDEM de inserção dos elementos

# Fazendo o import
from collections import OrderedDict

dicionario2 = OrderedDict({'a': 1,  'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario2.items():
    print(chave, valor)
"""

# Fazendo o import
from collections import OrderedDict

# Entendendo a diferença entre dict e OrderedDict

# Criando dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# sera que os dicionários acima sao os mesmos??
# Sim, pois para um dicionario comum a ordem nao importa!
print(dict1 == dict2)

# Criando dicionários com o ordered dict

dict01 = OrderedDict({'a': 1, 'b': 2})
dict02 = OrderedDict({'b': 2, 'a': 1})
# Será que os dicionários acima são os mesmos??
# Não eles não são, pois nesse caso a ordem importa!
print(dict01 == dict02)
