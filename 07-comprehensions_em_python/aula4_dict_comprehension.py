"""
Dictionary comprehension

Pense no seguinte:
Se quisermos criar uma lista fazemos, definimos da seguinte maneira:

 lista = [1, 2, 3, 4]

Se quisermos criar uma tupla, definimos da seguinte maneira:
tupla = (1, 2, 3, 4, 5) ou 1, 2, 3, 4, 5

Se quisermos criar um set (conjunto), definimos da seguinte maneira:

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário, definimos da seguinte maneira:

dicionario = {
             'a': 1,
             'b': 2,
             'c': 3,
             'd': 4
 }


# Sintaxe do dict comprehension

{chave: valor for valor in iterável}

Note a similaridade com o list comprehension

[valor for valor in iterável]


# Exemplos

dicionario = {
             'a': 1,
             'b': 2,
             'c': 3,
             'd': 4
 }

quadrado = {chave: valor**2 for chave, valor in dicionario.items()}

print(quadrado)

# Exemplos

Num = [1, 1, 2, 3, 4, 5, 5]

print({valor: valor**2 for valor in Num})

# Passamos a string como chave
chaves = 'abcde'

# Passamos os dados da lista como valor
valores = [1, 2, 3, 4, 5]

print({chaves[i]: valores[i] for i in range(0, len(chaves))})
"""

# Exemplo com logica condicional

numeros = [1, 2, 3, 4, 5]

print({num: ('par' if num % 2 == 0 else 'impar') for num in numeros})
