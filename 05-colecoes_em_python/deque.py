"""
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance

"""


# Importando
from collections import deque


# Criando um deque
deq = deque('string')
print(deq)
print(type(deq))

# adicionando ao final da lista
deq.append('y')
print(deq)

# adicionando no inicio da lista
deq.appendleft('a')
print(deq)

# Removendo elementos

# >>> Removendo a direita
print(deq.pop())
print(deq)

# >>> Removendo a esquerda

print(deq.popleft())
print(deq)
