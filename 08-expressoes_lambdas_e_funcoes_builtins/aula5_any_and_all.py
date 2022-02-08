"""
Any and All

all() -> retorna True se todos os elementos do iterável são verdadeiros  ou ainda se o iterável está vazio
         interessante usar list comprehension
# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

# lista vazia
print(all([]))

# tupla
print(all((1, 2, 3, 4)))

# set
print(all({1, 2, 3, 4}))

# string
print(all('Greek University'))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

# OBS: Um iterável vazio convertido em boolean é false, mas o all() entende como true
print(all([letra for letra in 'eio' if letra in 'casa']))
True
print(all(num for num in [4, 2, 10, 6, 8] if num % 2 == 0))
True

# any() -> Retornar True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False.

print(any([0, 1, 2, 3, 4, 5]))
True
print(any([]))
False
print(any([False, [], 0, {}, ()]))
False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
True
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
