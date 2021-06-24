"""
Expressões lambdas
 Map

Mapear valor para uma função


# Exemplo 1 - Queremos calcular a area de um circulo de raio r
from math import pi


def area(r):
    # Calcula area de um circulo de raio r
    return pi * r ** 2


print(area(2))
print(area(5.3))

# Se tivéssemos uma lista, poderíamos usar um for

raios = [2., 5., 7.1, 0.3, 1.]
areas = []

for i in raios:
    areas.append(area(i))

print(areas)


# Forma 2 -  usando um map, que é uma função que recebe dois parâmetros.
# o primeiro é uma função, o segundo um iterável

areas2 = map(area, raios)
print(type(areas2))
print(list(areas2))


# Forma 3 - O mais comum é passar uma expressão lambda no lugar da função
# A ideia é deixar o código mais limpo

print(list(map(lambda r: pi * r**2, raios)))


# OBS:
# Após utilizar a função map() o resultado é zerado depois de utilizado. Esse recurso
# é interessante porque limpa a memória.


# Para fixar o uso do map()

# 1 - temos dados iteráveis dados = a1, a2, a3, ..., an
# 2 - temos uma função f(x)
# 3 - Utilizamos a função map(f(x), dados) que deve mapear cada elemento do conjunto de dados aplicado na função.
# 4 - O objeto map gerado é do tipo f(a1), f(a2), f(a3), ..., f(an)
"""

# Exemplo de conversão de temperatura
Temperaturas_celcius = [('Berlin', 29), ('Rio de Janeiro', 40), ('Cairo', 36), ('São Paulo', 34), ('Los Angeles', 26),
           ('Londres', 22), ('Amsterdã', 34)]

print(Temperaturas_celcius)

# conversão para escala Fahrenheit: F = (9/5) * C + 32.0
Temperatura_Fahrenheit = lambda dado: (dado[0],  (9/5) * dado[1] + 32.0)

print(list(map(Temperatura_Fahrenheit, Temperaturas_celcius)))
print("\n")
