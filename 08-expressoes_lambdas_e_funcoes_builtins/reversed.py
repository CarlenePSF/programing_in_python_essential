"""
Reversed

OBS: O reversed nao deve ser confundido com a funcao reverse() que so funciona para listas.
#>>> lista = [1, 2, 3, 4]
#>>> print(lista)
[1, 2, 3, 4]
#>>> lista.reverse()
#>>> print(lista)
[4, 3, 2, 1]


A funcao reversed() funciona com QUALQUER iteravel!!

A caracteristica mais interessante e o tipo de dado que a funcao reversed retorna, chamando de
list_reverseiterator object

"""

# Exemplo
lista = [1, 2, 3, 4]

print(reversed(lista))
# <list_reverseiterator object at 0x7fee103f8310>
print(type(reversed(lista)))
#<class 'list_reverseiterator'>


# ----------- podemos converter o elemento retornado ------------

# lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# conjunto - nao guarda ordem!!
print(set(reversed(lista)))

# ---------- Podemos iterar sobre o reversed ----------
for letra in reversed('Geek Univeristy'):
    print(letra, end='')


# ---------- Sem o uso do loop for --------------------
print('\n')
print(''.join(list(reversed('Geek University'))))

# ------ Usando o slice de string --- modo pythonico
print('Geek University'[::-1])

# --------- Sequencia de numeros invertida ------------
for num in reversed(range(0, 10)):
    print(num)
