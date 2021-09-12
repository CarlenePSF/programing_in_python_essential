"""
List comprehension

Utilizando list comprehension, podemos gerar novas listas com
dados processados a partir de outro iterável.

# Sintaxe sobre a list comprehension

[dado for dado in iterável]

#Exemplos

lista = [1, 2, 3, 4, 5]

res = [num**2 for num in lista]

print(res)

Para entender melhor o que está acontecendo, vamos dividir a expressão em duas partes:
- A primeira parte : for num in lista
- A segunda parte: num**2 (potencia do numero presente na lista)

# Mais exemplos

from math import sqrt, sin, pi

# Exemplos

lista = [1, 2, 3, 4, 5]

res1 = [num**2 for num in lista]
res2 = [sqrt(num**2) for num in lista]

print(res1)
print(res2)


def function(valor):
    return sin(valor*pi)


res3 = [function(num) for num in lista]
print(res3)


# List comprehension x loop

# >>> Exemplo usando loop

lista2 = [1, 2, 3, 4, 5]
print(lista2)

lista3 = []
for numero in lista2:
    num = numero*2
    lista3.append(num)


print(lista3)


# >>> Exemplo utilizando list comprehension
# observe que uma única linha pode ser usada para executar a mesma tarefa!!

print([numero*2 for numero in lista2])

"""


# Exemplo 2
nome = 'Geek University'

print([letra.upper() for letra in nome])


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([letra[0].upper() + letra[1:] for letra in amigos])


# Exemplo 3

print([numero*3 for numero in range(1, 10)])


# Exemplo 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.1415]])


# Exemplo 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
