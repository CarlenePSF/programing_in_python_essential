"""
Mapas -> conhecidos em python como dicionarios

Dicionarios em python sao representados por chaves{}

# como iterar sobre dicionarios

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

for chave in dictionary:
    print(chave)

for chave in dictionary:
    print(dictionary[chave])

for chave in dictionary:
    print(f'Na chave {chave} esta o valor {dictionary[chave]}')

# acessando chaves

print(dictionary)
print(dictionary.keys())

for chave in dictionary.keys():
    print(dictionary[chave])

# acessando os valores

print(dictionary.values())

for valor in dictionary.values():
    print(valor)

# Desempacotando dicionarios

print(dictionary.items())

for chave, valor in dictionary.items():
    print(f'chave = {chave} e valor = {valor}')

"""
# Soma*, valor max*, valor mim*, tamanho
# * somente se os valores forem inteiros ou reais (float)

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
