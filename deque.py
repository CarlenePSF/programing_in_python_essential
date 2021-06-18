"""
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance

"""
#Improtando
from collections import deque

#Criando um deque
deq = deque('string')
print(deq)
print(type(deq))

#diciona ao final da lista
deq.append('y')
print(deq)

#adiciona no inicio da lista
deq.appendleft('a')
print(deq)

#Removendo elementos

#>>> Removendo a direita
print(deq.pop())
print(deq)

#>>> Removendo a esquerda

print(deq.popleft())
print(deq)
