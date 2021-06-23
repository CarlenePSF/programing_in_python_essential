"""
Set comprehension

OBS: Lembre-se que os conjuntos não são ordenados

Lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

# A sintaxe é parecida com o dictionary comprehension, mas sem o parametro para a chave

veja:
 dic comprehension
 {chave: valor for chave, valor in iterável}

 set comprehension
 {valor for valor in iterável}

# Exemplos 01

conjunto = {num for num in range(1, 7)}
print(conjunto)

# Exemplo 02

conjunto2 = {x**2 for x in range(10)}
print(conjunto2)


# Desafio: Faça uma alteração na estrutura acima para gerar um dicionario ao invés de um set.

dicio = {x: x**2 for x in range(10)}
print(dicio)
"""

# Exemplo com string

letras = {letra for letra in 'Geek University'}

print(letras)
