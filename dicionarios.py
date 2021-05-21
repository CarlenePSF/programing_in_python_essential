"""
Trabalhando com dicionarios
Em alguma linguagens de programação, os dicionários python são
conhecidos por mapas.py

 - Dicionarios são coleções do tipo chave/valor
 - No dicionarios o conjunto chave/valor fica explicito!!

 dicionários são representados por chaves

 print(type({}))

 OBS: Sobre dicionários
      - Chave e valor são separados por dois pontos 'chave':'valor'
      - Tanto a chave quanto o valor podem ser de qualquer tipo de dados
      - Podemos misturar qualquer tipo de dado num dicionário

# Forma mais comum para criação de dicionários
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'fr': 'França'
}
print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(
    br='Brasil',
    eua='Estados Unidos',
    fr='França'
)
print(paises)
print(type(paises))


# acessando elementos
# Forma 1 - acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['fr'])

# OBS: Caso se tente fazer acesso a uma chave que não existe teremos um erro tipo KeyError
# print(paises['ru'])

# Forma 2 - acessando via get (forma recomendada)
print(paises.get('br'))
print(paises.get('eua'))
# não fornece erro mas uma tipo de dado none
print(paises.get('ru'))

# Serve para verificar se tem um elemento no dicionário
pais = paises.get('br')
if pais:
    print('Encontrei o país!')
else:
    print('Não encontrei o país!')

russia = paises.get('ru')

if russia:
    print('Encontrei o país!')
else:
    print('Não encontrei o país!')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('fr', 'Não encontrado')
print(f'Encontrei o pais {pais}')

# Verificando se uma chave está no dicionário
print('br' in paises)
print('ru' in paises)
# não busca valor, busca pela chave
print('Japão' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos usar qualquer tipo de dado (int, float, string. boolean),
# inclusive listas, tupla dicionario como chaves de dicionarios
# Tuplas, por exemplo, são bastante interessantes de serem utilizadas como chaves de dicionários,
# pois as mesmas são imutáveis


localidade = {
    (35.698, 39.6917): 'Escritorio em Tóquio',
    (35.654, 396717): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo'
}
print(localidade)
print(type(localidade))

# adicionando elementos em um dicionario
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'fr': 'França',
    'jp': 'Japão'
}
# Forma 1 - mais comum
paises['pt'] = 'Portugal'
print(paises)

# Forma 2
novo_dado = {'ru': 'Russia'}
paises.update(novo_dado)
print(paises)

#atualizando dados em um dicionario
#forma 1
paises['br'] = 'Brasil2'
print(paises)

#forma 2
paises.update({'br': 'Brazil'})
print(paises)

# Conclusao 1: A forma de adicionar novos elementos ou atualizar dados e a mesma
# Conclusao 2: Em dicionarios Nao podemos ter chaves repetidas!!!!!

# Remover dados de um dicionario
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'fr': 'França',
    'jp': 'Japão'
}
print(paises)

# OBS1: Sempre precisamos informar a chave que esta contida no dict
#       se a chave nao estiver no dict obtermos um KeyError
# OBS2: Ao removermos um objeto, o valor deste objeto e sempre retornado
# OBS3: Se a chave nao existir sera gerado um KeyError

# Forma 1 - forma mais comum
ret = paises.pop('jp')
print(ret)
print(paises)

# Forma 2
del paises['eua']
print(paises)

# onde utilizar colecoes?

# Imagine que voce tenha um comercio eletronico, onde temos um carrinho de compras
# no qual adicionamos produtos
'''
carrinho de compras1:
    produtos 1:
        nome
        quantidade
        preco
    produtos 2:
        nome
        quantidades
        preco
'''
# pergunta: Poderiamos utilizar uma lista para isso? Sim!!!

carrinho = []
product1 = ['PlayStation 4', 1, 2300.00]
product2 = ['Assassins Creed', 1, 150.00]

carrinho.append(product1)
carrinho.append(product2)
print(carrinho)

# Teriamos que saber qual e o indice de cada informacao no produto


# 2 - Poderiamos usar Tuplas? Sim!!!

product01 = ('PlayStation 4', 1, 2300.00)
product02 = ('Assassins Creed', 1, 150.00)
carrinho = (product01, product02)
print(carrinho)

# 2 - Poderiamos usar dicionarios? Sim!!! e ainda e mais adequado
#     pois as informacoes sao mais detalhadas.
carrinho = []

produto1 = {'nome': 'PlayStation 4',
            'quantidade': 1,
            'preco': 2300.00
            }
produto2 = {'nome': 'Assassins Creed',
            'quantidade': 1,
            'preco': 150.00
            }

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

print(carrinho[0])
print(carrinho[1])

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(dictionary)

# Limpando o dicionario

dictionary.clear()
print(dictionary)



# copiando uma dicionario para outro

# Forma 1 -  deep copy
novo = dictionary.copy()
print(novo)
novo['d'] = 4
print(novo)

# Forma 2 - shallow copy (pois altera o original tambem!!!)
# tomar cuidado com essa forma de copiar!!!
novo = dictionary
print(novo)
novo['d'] = 4
print(novo)
print(dictionary)
"""


# Forma nao usual de criacao de dicionario
dicionario = {}.fromkeys('a', 1)
print(dicionario)

# No exemplo abaixo, com o metodo .fromkeys() deve receber dois parametros,
# onde um e um iteravel e o outro valor.
# Ele vai gerar para cada valor do iteravel uma chave
# e vai distribuir para esta chave  o valor iteravel

outrodict = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(outrodict)

outrodict1 = {}.fromkeys(range(1, 11), 'novo')
print(outrodict1)
