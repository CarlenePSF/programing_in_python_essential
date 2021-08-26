"""
Tipo Numeric -> o mesmo de (int)

tipo float -> tipo real, decimal casas decimais

Obs: o separador de casas decimais é o ponto (.)
"""
from math import sqrt

num = 1_000_000
print(num)


def main():
    a = 3.0
    b = 4.0
    soma = a + b
    print(f'A soma de {a} + {b} eh igual a {soma}')


main()

valor = 1, 44
print(valor)
print(type(valor))

valor = 1.44
print(valor)
print(type(valor))

res = int(valor)
print(res)


# Complex numbers - qualquer número com unidade imaginaria no python sendo o (j)

var = 2j
var2 = sqrt(4)
print(var2)
