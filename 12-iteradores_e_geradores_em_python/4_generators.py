"""
Geradores

Geradores (generators) são iteradores (iterators)

OBS: O contrário não é verdadeiro. Ou seja, iterators não são generators;

Outras informações:

- Generators podem ser criados com funções geradoras
- funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras.

Diferenças entre funções e generators functions (funções geradoras)

-----------------------------------------------------------------------------------------
| Funções                                   |   Generators functions                   |
-----------------------------------------------------------------------------------------
| utiliza o return                          |   utiliza o yield                        |
| somente um retorno                        |  pode usar mais de um yield              |
| quando executada, retorna um valor        |  Quando executada retorna um generator   |
|---------------------------------------------------------------------------------------


# Exemplo de generator function
# OBS: Uma função geradora não é um generator. Ela gera um generator.


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(5)
# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # retorna StopIteration Error

# imprime até 10
gen = conta_ate(10)

for num in gen:
    print(num)
"""


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1



