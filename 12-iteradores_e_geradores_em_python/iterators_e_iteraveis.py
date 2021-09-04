"""
Iteradores (iterators) e iteráveis (iterables)

Iterator ->
    * Um objeto que pode ser iterado
    * Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterável (iterable)->
    * Um objeto que irá retornar um iterator quando a função iter() for chamada.


# ---- Exemplos de iteráveis

# Exemplos de iteráveis
nome = 'Geek'  # string
numeros = [1, 2, 3, 4]  # listas
iter1 = iter(nome)
iter2 = iter(numeros)


print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
# print(next(iter1))  # Error StopIteration pois não tem mais nada para iterar

print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))

"""
nome = 'Geek'
for letra in nome:
    print(letra)

print('\n')
# É equivalente a
iterador = iter(nome)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
