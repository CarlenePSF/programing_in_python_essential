"""
Teste de velocidade com expressões geradoras

#  ----- Diferença entre generators e generator expression -----
# Generators (geradores)


def numeros():
    for num in range(1, 10):
        yield num


gen1 = numeros()

print(gen1)  # generator
print(next(gen1))
print(next(gen1))


# Generator expression

gen2 = (num for num in range(1, 10))  # generator expression <genexpr>
print(gen2)

print(next(gen2))
print(next(gen2))

"""

# Realizando o teste de velocidade
import time


# generator expression
gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))

gen_tempo = time.time() - gen_inicio


# list comprehension
list_inicio = time.time()
print(sum([num for num in range(1, 100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator expression: {round(gen_tempo, 2)}')
print(f'List comprehension: {round(list_tempo, 2)}')


# Generator expression: 4.59s
# List comprehension: 8.49s
